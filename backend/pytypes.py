from pydantic import BaseModel
from datetime import date

class FeatureRequestPost(BaseModel):
    title: str
    description: str

class FeatureRequest(BaseModel):
    id: int
    title: str
    description: str
    created_at: date
    rating: int

class FeatureRequestResponse(BaseModel):
    message: str
    id: int
