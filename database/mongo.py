from motor.motor_asyncio import AsyncIOMotorClient
from utils.config import MONGO_URI
from utils.logger import logger

mongo_client = AsyncIOMotorClient(MONGO_URI)

db = mongo_client["telegram_deployer"]

logger.info("MongoDB connected successfully")
