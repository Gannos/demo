from tortoise import Tortoise
import os
from dotenv import load_dotenv

load_dotenv()

# review this
DB_URL: str = os.getenv("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("DATABASE_URL environment variable must be set.")

async def init_db():
    try:
        await Tortoise.init(
            db_url=DB_URL,
            modules={
                "models": ["models"]
            }
        )
        await Tortoise.generate_schemas()
    except Exception as e:
        print(f"Error during database initialization: {e}")
        await close_db()
        raise # python idiom. re-raises exception with complete traceback

async def close_db():
    try:
        await Tortoise.close_connections()
    except Exception as e:
        print(f"Error closing connections: {e}")
