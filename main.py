import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document, PydanticObjectId
from fastapi.middleware.cors import CORSMiddleware
from typing import List

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

# CRUD Endpoints
@app.post("/items/", response_model=StoreItem)
async def create_item(item: StoreItem):
    await item.insert()
    return item

@app.get("/items/")
async def get_items():
    items = await StoreItem.find_all().to_list()
    return items

@app.delete("/delete/{item_id}")
async def delete_item(item_id: PydanticObjectId):
    item = await StoreItem.get(item_id)
    if item:
        await item.delete()
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/")
async def read_index():
    return FileResponse("Frontend/Home.html")


@app.get("/index")
async def read_profile():
    return FileResponse("Frontend/index.html")

@app.get("/inputgenerated")
async def read_input_generated():
    return FileResponse("Frontend/InputGenerated.html")

# List Complete page
@app.get("/listcomplete")
async def read_list_complete():
    return FileResponse("Frontend/ListComplete.html")

# Profile page
@app.get("/profile")
async def read_profile():
    return FileResponse("Frontend/Profile.html")

# Price Update page
@app.get("/priceupdate")
async def read_price_update():
    return FileResponse("Frontend/PriceUpdate.html")

# Filter page
@app.get("/filter")
async def read_filter():
    return FileResponse("Frontend/Filter.html")

# SL1 page
@app.get("/sl1")
async def read_sl1():
    return FileResponse("Frontend/SL1.html")



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
