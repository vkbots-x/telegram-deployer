from fastapi import FastAPI

web_app = FastAPI()


@web_app.get("/")
async def root():
    return {
        "status": "running"
    }
