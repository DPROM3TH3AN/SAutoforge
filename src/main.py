import os
import uvicorn
from fastapi import FastAPI
from api import router as api_router

app = FastAPI(
    title="SuiAutoforge",
    description="An API to generate smart contract using GPT",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "welcome to autoforge"}

if __name__ == "__main__":
   host = os.getenv("HOST", "127.0.0.1")
   port = int(os.getenv("PORT", 8000))
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)