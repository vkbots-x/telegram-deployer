from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_URI = getenv("MONGO_URI")

OWNER_ID = int(getenv("OWNER_ID"))

ENCRYPTION_KEY = getenv("ENCRYPTION_KEY")
RENDER_URL = getenv("RENDER_URL")
