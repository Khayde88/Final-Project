import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document, PydanticObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_index():
    try:
        return FileResponse("Home.html")  # Direct path to Home.html
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index file not found")

@app.get("/Catagories")
async def read_profile():
    return FileResponse("Catagories.html")

@app.get("/inputgenerated")
async def read_input_generated():
    return FileResponse("InputGenerated.html")

# List Complete page
@app.get("/listcomplete")
async def read_list_complete():
    return FileResponse("ListComplete.html")

# Profile page
@app.get("/profile")
async def read_profile():
    return FileResponse("Profile.html")

# Price Update page
@app.get("/priceupdate")
async def read_price_update():
    return FileResponse("PriceUpdate.html")

# Filter page
@app.get("/filter")
async def read_filter():
    return FileResponse("Filter.html")

# SL1 page
@app.get("/sl1")
async def read_sl1():
    return FileResponse("SL1.html")
@app.delete("/delete/{item_id}")
async def delete_item(item_id: PydanticObjectId):
    item = await Sample.get(item_id)
    if item:
        await item.delete()
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

class Sample(Document):
    name: str

async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    await init_beanie(database=client.grocery_db, document_models=[Sample])

@app.on_event("startup")
async def startup_event():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
