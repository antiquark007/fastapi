from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)#Configures the logging system for the application.
logger = logging.getLogger(__name__)# Creates a logger instance for the current module.

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

mongodb = MongoDB()

async def connect_to_mongo():
    try:
        mongodb.client = AsyncIOMotorClient("url of the cluster")
        mongodb.db = mongodb.client["myDB"]
        logger.info("Connected to MongoDB!")
    except PyMongoError as e:
        logger.error(f"Failed to connect to MongoDB: {e}")#by simple print not a good way to handel the error
        raise e

async def close_mongo_connection():
    try:
        if mongodb.client:
            mongodb.client.close()
            logger.info("Disconnected from MongoDB!")
    except PyMongoError as e:
        logger.error(f"Failed to disconnect from MongoDB: {e}")
        raise e