import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pymongo import MongoClient
from api import groceries

app = FastAPI()


# MongoDB connection setup
client = MongoClient(
    "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)  # Update with your MongoDB connection URI
db = client["grocery_db"]  # Replace 'grocery_db' with your desired database name
collection = db["grocery_items"]  # Collection name for grocery items


# Example route to test MongoDB connection
@app.get("/test_mongodb")
async def test_mongodb_connection():
    try:
        client.server_info()  # Test if connection is successful
        return {"message": "MongoDB connection successful"}
    except Exception as e:
        return {"message": f"MongoDB connection error: {str(e)}"}


# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Adjust as needed for your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def read_index():
    return FileResponse("./Frontend/Home.html")


app.mount("/", StaticFiles(directory="Frontend"), name="static")

app.include_router(groceries.router)

# Start the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
