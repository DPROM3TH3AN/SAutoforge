from fastapi import FastAPI

# --------------------------
# CRITICAL INTEGRATION POINT
# --------------------------
# Import the router from api.py module
from .api import router as api_router

app = FastAPI(
    title="SuiAutoforge",
    description="API for AI Smart Contract Generation",
    version="1.0.0"
)

# --------------------------
# ROUTER MOUNTING SECTION
# --------------------------
# Attach all endpoints from api.py under "/api" path
# This connects the main app with the API module
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome the SuiAutoforge"}
"""
if __name__ == "__main__":
    import uvicorn
    # Explicitly show imported components
    print("Loaded API Routes:", [route.path for route in app.routes if "api" in route.path])
    # Run the Uvicorn server
    uvicorn.run("main:app", host="0.0.0.0", port=8000)"""