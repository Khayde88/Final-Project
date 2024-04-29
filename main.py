# import uvicorn
# from fastapi import FastAPI, HTTPException, Form
# from starlette.responses import FileResponse
# from motor.motor_asyncio import AsyncIOMotorClient
# from beanie import init_beanie, Document, PydanticObjectId
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List
# from pymongo import MongoClient
# import pymongo

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# class StoreItem(Document):
#     date: str
#     stores: List[str]
#     location: str

#     class Settings:
#         collection = "store_items"

# # Initialize Beanie with the StoreItem Document model
# @app.on_event("startup")
# async def init_db():
#     client = AsyncIOMotorClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     await init_beanie(database=client.grocery_db, document_models=[StoreItem])

# # CRUD Endpoints
# @app.post("/items/", response_model=StoreItem)
# async def create_item(item: StoreItem):
#     await item.insert()
#     return item

# @app.get("/items/")
# async def get_items():
#     items = await StoreItem.find_all().to_list()
#     return items

# @app.delete("/delete/{item_id}")
# async def delete_item(item_id: PydanticObjectId):
#     item = await StoreItem.get(item_id)
#     if item:
#         await item.delete()
#         return {"message": "Item deleted successfully"}
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.get("/")
# async def read_index():
#     return FileResponse("./Frontend/Home.html")

# @app.get("/index")
# async def read_profile():
#     return FileResponse("./Frontend/index.html")

# @app.get("/inputgenerated")
# async def read_input_generated():
#     return FileResponse("./Frontend/InputGenerated.html")

# @app.get("/listcomplete")
# async def read_list_complete():
#     return FileResponse("./Frontend/ListComplete.html")

# @app.get("/profile")
# async def read_profile():
#     return FileResponse("./Frontend/Profile.html")

# @app.get("/priceupdate")
# async def read_price_update():
#     return FileResponse("./Frontend/PriceUpdate.html")

# @app.get("/filter")
# async def read_filter():
#     return FileResponse("./Frontend/Filter.html")

# @app.get("/sl1")
# async def read_sl1():
#     return FileResponse("./Frontend/SL1.html")
# #navigate to EL.html
# @app.get("/el")
# async def read_el():
#     return FileResponse("./Frontend/EL.html")

# # Trying to get the input from the user

# @app.post("/run-script")
# def run_script(input_data: str = Form(...)):
#     # Connect to MongoDB
#     client = MongoClient('mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
#     db = client['grocery_db']
#     collection = db['grocery_items']

#     # Write data to MongoDB
#     data = {"input": input_data}
#     collection.insert_one(data)

#     # Write data to MongoDB using pymongo
#     myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     mydb = myclient["grocery_db"]
#     mycol = mydb["SavedList"]

#     mydict = {
#         "date": "1/15/2023",
#         "stores": ["Target", "Whole Foods Market", "Fareway"],
#         "location": "Delete_test_2"
#     }

#     x = mycol.insert_one(mydict)

#     return {"message": "Data written to MongoDB successfully"}

# from bson import ObjectId

# @app.get("/read-saved-list")
# async def read_saved_list():
#     # Connect to MongoDB
#     client = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     db = client["grocery_db"]
#     col = db["SavedList"]

#     # Retrieve data from MongoDB
#     saved_data = list(col.find())

#     # Convert ObjectId to string in each item
#     for item in saved_data:
#         item['_id'] = str(item['_id'])

#     # Return the retrieved data
#     return saved_data

# @app.delete("/delete-saved-item/{item_id}")
# async def delete_saved_item(item_id: str):
#     # Connect to MongoDB
#     client = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     db = client["grocery_db"]
#     col = db["SavedList"]

#     # Convert item_id to ObjectId
#     try:
#         obj_id = ObjectId(item_id)
#     except:
#         raise HTTPException(status_code=400, detail="Invalid item ID")

#     # Delete item from MongoDB
#     result = col.delete_one({"_id": obj_id})

#     if result.deleted_count == 1:
#         return {"message": "Item deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")

# # Import necessary modules
# from fastapi import HTTPException

# # Update endpoint for modifying existing items
# @app.put("/update/{item_id}")
# async def update_item(item_id: PydanticObjectId, updated_item: StoreItem):
#     # Get the existing item
#     existing_item = await StoreItem.get(item_id)
    
#     # If the item doesn't exist, raise HTTPException
#     if not existing_item:
#         raise HTTPException(status_code=404, detail="Item not found")
    
#     # Update the fields of the existing item
#     existing_item.date = updated_item.date
#     existing_item.stores = updated_item.stores
#     existing_item.location = updated_item.location
    
#     # Save the updated item
#     await existing_item.save()
    
#     return existing_item

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)

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
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

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

class StoreItem(Document):
    date: str
    stores: List[str]
    location: str

    class Settings:
        collection = "store_items"

# Initialize Beanie with the StoreItem Document model
@app.on_event("startup")
async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    await init_beanie(database=client.grocery_db, document_models=[StoreItem])
    logger.info("Beanie initialized successfully")

# CRUD Endpoints
@app.post("/items/", response_model=StoreItem)
async def create_item(item: StoreItem):
    await item.insert()
    logger.info("Item created successfully")
    return item

@app.get("/items/")
async def get_items():
    items = await StoreItem.find_all().to_list()
    logger.info("Items retrieved successfully")
    return items

@app.delete("/delete/{item_id}")
async def delete_item(item_id: PydanticObjectId):
    item = await StoreItem.get(item_id)
    if item:
        await item.delete()
        logger.info(f"Item with ID {item_id} deleted successfully")
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")





@app.get("/")
async def read_index():
    return FileResponse("./Home.html")

@app.get("/index")
async def read_profile():
    logger.info("Index file requested")
    return FileResponse("./index.html")

@app.get("/inputgenerated")
async def read_input_generated():
    return FileResponse("./InputGenerated.html")

@app.get("/catagories")
async def read_input_generated():
    return FileResponse("./Catagories.html")

@app.get("/listcomplete")
async def read_list_complete():
    return FileResponse("./ListComplete.html")

@app.get("/profile")
async def read_profile():
    return FileResponse("./Profile.html")

@app.get("/priceupdate")
async def read_price_update():
    return FileResponse("./PriceUpdate.html")

@app.get("/filter")
async def read_filter():
    return FileResponse("./Filter.html")

@app.get("/sl1")
async def read_sl1():
    return FileResponse("./SL1.html")
#navigate to EL.html

# Trying to get the input from the user

@app.post("/run-script")
def run_script(input_data: str = Form(...)):
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['grocery_db']
    collection = db['grocery_items']

    # Write data to MongoDB
    data = {"input": input_data}
    collection.insert_one(data)

    # Write data to MongoDB using pymongo
    myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    mydb = myclient["grocery_db"]
    mycol = mydb["SavedList"]

    mydict = {
        "date": "1/15/2023",
        "stores": ["Target", "Whole Foods Market", "Fareway"],
        "location": "Delete_test_2"
    }

    x = mycol.insert_one(mydict)

    return {"message": "Data written to MongoDB successfully"}

from bson import ObjectId
@app.get("/get-grocery-items")
async def get_grocery_items():
    client = MongoClient('mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['grocery_db']
    collection = db['grocery_items']

    items = list(collection.find({}))

    # Convert each item's ObjectId to string
    for item in items:
        item['_id'] = str(item['_id'])

    return items

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

# Import necessary modules
from fastapi import HTTPException

# # Update endpoint for modifying existing items
# @app.put("/update/{item_id}")
# async def update_item(item_id: PydanticObjectId, updated_item: StoreItem):
#     # Log the received item ID
#     logger.info(f"Received request to update item with ID: {item_id}")
#     # Get the existing item
#     existing_item = await StoreItem.get(item_id)
    
#     # If the item doesn't exist, raise HTTPException
#     if not existing_item:
#         logger.error(f"Item with ID {item_id} not found")
#         raise HTTPException(status_code=404, detail="Item not found")
    
#     # Update the fields of the existing item
#     existing_item.date = updated_item.date
#     existing_item.stores = updated_item.stores
#     existing_item.location = updated_item.location
    
#     # Save the updated item
#     await existing_item.save()
#     logger.info(f"Item with ID {item_id} updated successfully")
#     return existing_item

# Update endpoint for modifying existing items
@app.put("/update/{item_id}")
async def update_item(item_id: str, updated_item: StoreItem):
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

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)