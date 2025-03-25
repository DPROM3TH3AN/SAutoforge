import os
import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="SuiAutoforge",
    description="An API to generate smart contract using GPT",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "welcome to autoforge"}

from .api import router as api_router
app.include_router(api_router)

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8000))
   uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)