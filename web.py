from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
@app.head("/")
async def home():

    return JSONResponse(
        {
            "status": "running"
        }
    )
