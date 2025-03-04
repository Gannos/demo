from fastapi import FastAPI, HTTPException, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from database import init_db, close_db
from typing import List, Any

import json

from models import FeatureRequest, Rating
from pytypes import FeatureRequestPost, FeatureRequestResponse
from pytypes import FeatureRequest as FeatureRequestType

import logging
logger = logging.getLogger(__name__)

app = FastAPI()
active_connections: list[WebSocket] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Change this!
    allow_credentials=True,  # Allows cookies, auth headers
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Upgrade", "Connection"], # Necessary for websockets
)

async def rate_request(message: dict[str, Any]) -> dict[str, Any]:
    logger.error("Updating rating.")
    try:
        feature_request = await FeatureRequest.get(id=message['id']).select_related('rating')
        direction = message['direction']
        old_rating = feature_request.rating.rating
        new_rating = old_rating + (1 if direction == "up" else -1)
        feature_request.rating.rating = new_rating
        await feature_request.rating.save()
        return { "type": "rate", "rating": new_rating, "id": message['id'] }
    except Exception as e:
        pass

async def update_requests(message: dict[str, Any]) -> dict[str, Any]:
    try:
        feature_requests = await FeatureRequest.all().select_related("rating")
        return [
            {
                "id": req.id,
                "title": req.title,
                "description": req.description,
                "created_at": req.created_at,
                "rating": req.rating.rating if req.rating else 0
            }
            for req in requests
        ]
    except Exception as e:
        pass

async def process_message(message: dict[str, Any]) -> str:
    logger.error("Processing message: %s", message['id'])
    function_pointers: dict[str, Any] = {
        # maps msg_type to function
        "rate": rate_request,
        "update_requests": update_requests,
        # additional functions go here
    }
    for _type, fct in function_pointers.items():
        if _type == message['type']:
            response = await fct(message)
            logger.error("Finished processing message.")
            return response
    logger.error("ERROR: unknown fct")
    response = "Not found."
    return response


@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data_string: str = await websocket.receive_text()
            message: dict[str: Any] = json.loads(data_string)
            response = await process_message(message)
            for connection in active_connections:
                try:
                    await connection.send_text(json.dumps(response))
                except Exception as e:
                    active_connections.remove(connection)
    except WebSocketDisconnect:
        active_connections.remove(websocket)

@app.on_event("startup")
async def startup() -> None:
    try:
        await init_db()
    except Exception as e:
        print(f"Error during startup: {e}")
        raise

@app.on_event("shutdown")
async def shutdown() -> None:
    try:
        await close_db()
    except Exception as e:
        print(f"Error during shutdown: {e}")
        raise

@app.get("/api/feature_request", response_model=List[FeatureRequestType])
async def get_feature_requests() -> List[FeatureRequestType]:
    print("Getting feature requests.")
    requests: List[FeatureRequest] = await FeatureRequest.all().select_related("rating")
    return [
        FeatureRequestType(
            id=req.id,
            title=req.title,
            description=req.description,
            created_at=req.created_at,
            rating=req.rating.rating if req.rating else 0  # map Rating.rating to an int
        )
        for req in requests
    ]
    return requests

@app.post("/api/feature_request/add")
async def post_feature_request(request: FeatureRequestPost) -> FeatureRequestResponse:
    print("Adding feature request.")
    try:
        rating = await Rating.create()
        feature: FeatureRequestPost = await FeatureRequest.create(
            title=request.title,
            description=request.description,
            rating=rating
        )
        return FeatureRequestResponse(message="Feature request created.", id=feature.id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
