from fastapi import APIRouter, HTTPException
from db import mongodb

router = APIRouter()


# Create grocery item
@router.post("/api/groceries")
async def add_grocery(item_data: dict):
    try:
        result = mongodb.add_grocery(item_data)
        return {
            "message": "Grocery item added successfully",
            "inserted_id": str(result.inserted_id),
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error adding grocery item: {str(e)}"
        )


# Get all grocery items
@router.get("/api/groceries")
async def get_groceries():
    try:
        groceries = mongodb.get_groceries()
        return {"groceries": groceries}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching groceries: {str(e)}"
        )
