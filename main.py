import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from api import groceries
from db import mongodb

app = FastAPI()

# Initialize MongoDB client connection
mongodb.initialize_mongodb()

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Adjust as needed for your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Example route to test MongoDB connection
@app.get("/test_mongodb")
async def test_mongodb_connection():
    try:
        mongodb.client.server_info()  # Test if connection is successful
        return {"message": "MongoDB connection successful"}
    except Exception as e:
        return {"message": f"MongoDB connection error: {str(e)}"}


# Route to serve index.html from frontend
@app.get("/")
async def read_index():
    return FileResponse("./Frontend/Home.html")


# Mount static files directory for frontend
app.mount("/", StaticFiles(directory="Frontend"), name="static")

# Include router for groceries API
app.include_router(groceries.router)

# Start the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
