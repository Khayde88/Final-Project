import uvicorn
from fastapi import FastAPI, HTTPException, Form
from starlette.responses import FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document, PydanticObjectId
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pymongo import MongoClient
from bson import ObjectId
import pymongo
import logging


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class SavedListItem(Document):
    date: str
    stores: List[str]
    location: str

    class Settings:
        collection = "SavedList"

# Initialize Beanie with the SavedListItem Document model
@app.on_event("startup")
async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    await init_beanie(database=client.grocery_db, document_models=[SavedListItem])
    logger.info("Beanie initialized successfully")

# CRUD Endpoints
@app.post("/run-script")
async def run_script(data: dict):
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['grocery_db']
    collection = db['SavedList']

    # Write data to MongoDB
    collection.insert_one(data)

    return {"message": "Data written to Saved List successfully"}

@app.get("/read-saved-list")
async def read_saved_list():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["grocery_db"]
    col = db["SavedList"]

    # Retrieve data from MongoDB
    saved_data = list(col.find())

    # Convert ObjectId to string in each item
    for item in saved_data:
        item['_id'] = str(item['_id'])

    # Return the retrieved data
    return saved_data

@app.delete("/delete-saved-item/{item_id}")
async def delete_saved_item(item_id: str):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["grocery_db"]
    col = db["SavedList"]

    # Convert item_id to ObjectId
    try:
        obj_id = ObjectId(item_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid item ID")

    # Delete item from MongoDB
    result = col.delete_one({"_id": obj_id})

    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.put("/update/{item_id}")
async def update_item(item_id: str, updated_item: SavedListItem):
    # Log the received item ID
    logger.info(f"Received request to update item with ID: {item_id}")
    
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["grocery_db"]
    col = db["SavedList"]

    # Convert item_id to ObjectId
    try:
        obj_id = ObjectId(item_id)
    except:
        logger.error("Invalid item ID format")
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    # Update the item in MongoDB
    result = col.update_one(
        {"_id": obj_id},
        {"$set": {
            "date": updated_item.date,
            "stores": updated_item.stores,
            "location": updated_item.location
        }}
    )

    # Check if the item was updated successfully
    if result.matched_count == 0:
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")

    logger.info(f"Item with ID {item_id} updated successfully")

    # Return the updated item
    return updated_item

@app.get("/")
async def read_index():
    return FileResponse("./Frontend/Home.html")
@app.get("/el")
async def read_index():
    return FileResponse("./Frontend/EL.html")

@app.get("/home")
async def read_index():
    return FileResponse("./Frontend/Home.html")

@app.get("/index")
async def read_profile():
    logger.info("Index file requested")
    return FileResponse("./Frontend/index.html")

@app.get("/profile")
async def read_profile():
    return FileResponse("./Frontend/Profile.html")

@app.get("/priceupdate")
async def read_price_update():
    return FileResponse("./Frontend/PriceUpdate.html")

@app.get("/sl1")
async def read_sl1():
    return FileResponse("./Frontend/SL1.html")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)