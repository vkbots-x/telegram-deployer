from fastapi import FastAPI
from fastapi import Request

from bot.bot import app

web_app = FastAPI()


@web_app.get("/")
async def home():

    return {
        "status": "running"
    }


@web_app.post("/webhook")
async def webhook_handler(
    request: Request
):

    update = await request.json()

    await app.process_update(update)

    return {
        "ok": True
    }
