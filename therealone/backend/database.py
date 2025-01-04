from beanie import Document, init_beanie
from models.QuestModel import QuestMD
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import os
import logging

# logging.basicConfig(level=logging.DEBUG)

class Quests (Document, QuestMD):
    pass

async def init_db():
    logging.info("Initializing database connection...")
    mongo_url = create_mongo_url()
    # logging.critical ("the url is:                      "+mongo_url)
    try:
        client = AsyncIOMotorClient(mongo_url)
        await init_beanie(database=client["questlog"], document_models=[Quests])
        logging.info("Database connection initialized successfully.")
    except Exception as e:
        logging.critical(f"Error initializing database connection: {e}", exc_info=True)

def create_mongo_url():
    user_name = os.getenv("MONGO_USER", "rootuser") 
    password = os.getenv("MONGO_PASS", "rootpass")
    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", "27017")
    MONGO_URL = f"mongodb+srv://ofir12290:ns8kE8AsrKq5AVHn@questlogcl.mnfqa.mongodb.net/"
    # MONGO_URL = f"mongodb://{user_name}:{password}@{host}/questlog?retryWrites=true&w=majority&tls=true"

    # MONGO_URL = f"mongodb://{user_name}:{password}@{host}?retryWrites=true&w=majority&ssl=true&tlsInsecure=true"
    # MONGO_URL = f"mongodb://{user_name}:{password}@{host}:{port}/"
    return MONGO_URL
