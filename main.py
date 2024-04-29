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
    client = AsyncIOMotorClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
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
    return FileResponse("./Frontend/Home.html")


@app.get("/index")
async def read_profile():
    logger.info("Index file requested")
    return FileResponse("./Frontend/index.html")


@app.get("/inputgenerated")
async def read_input_generated():
    return FileResponse("./Frontend/InputGenerated.html")


@app.get("/listcomplete")
async def read_list_complete():
    return FileResponse("./Frontend/ListComplete.html")


@app.get("/profile")
async def read_profile():
    return FileResponse("./Frontend/Profile.html")


@app.get("/priceupdate")
async def read_price_update():
    return FileResponse("./Frontend/PriceUpdate.html")


@app.get("/filter")
async def read_filter():
    return FileResponse("./Frontend/Filter.html")


@app.get("/sl1")
async def read_sl1():
    return FileResponse("./Frontend/SL1.html")


# Login/Register files


@app.get("/login")
async def read_login():
    return FileResponse("./Frontend/login.html")


@app.get("/register")
async def read_register():
    return FileResponse("./Frontend/register.html")


# navigate to EL.html
@app.get("/el")
async def read_el():
    logger.info("EL file requested")
    return FileResponse("./Frontend/EL.html")


# Trying to get the input from the user


@app.post("/run-script")
def run_script(input_data: str = Form(...)):
    # Connect to MongoDB
    client = MongoClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    db = client["grocery_db"]
    collection = db["grocery_items"]

    # Write data to MongoDB
    data = {"input": input_data}
    collection.insert_one(data)

    # Write data to MongoDB using pymongo
    myclient = pymongo.MongoClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    mydb = myclient["grocery_db"]
    mycol = mydb["SavedList"]

    mydict = {
        "date": "1/15/2023",
        "stores": ["Target", "Whole Foods Market", "Fareway"],
        "location": "Delete_test_2",
    }

    x = mycol.insert_one(mydict)

    return {"message": "Data written to MongoDB successfully"}


from bson import ObjectId


@app.get("/read-saved-list")
async def read_saved_list():
    # Connect to MongoDB
    client = pymongo.MongoClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    db = client["grocery_db"]
    col = db["SavedList"]

    # Retrieve data from MongoDB
    saved_data = list(col.find())

    # Convert ObjectId to string in each item
    for item in saved_data:
        item["_id"] = str(item["_id"])

    # Return the retrieved data
    return saved_data


@app.delete("/delete-saved-item/{item_id}")
async def delete_saved_item(item_id: str):
    # Connect to MongoDB
    client = pymongo.MongoClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
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
    client = MongoClient(
        "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
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
        {
            "$set": {
                "date": updated_item.date,
                "stores": updated_item.stores,
                "location": updated_item.location,
            }
        },
    )

    # Check if the item was updated successfully
    if result.matched_count == 0:
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")

    logger.info(f"Item with ID {item_id} updated successfully")

    # Return the updated item
    return updated_item


### USER AUTHENTICATION

from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pymongo import MongoClient
from datetime import datetime, timedelta

# JWT Settings
SECRET_KEY = "SecretKey1234"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB Connection
MONGO_URI = (
    "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/grocery_db"
)
client = MongoClient(MONGO_URI)
db = client["grocery_db"]
users_collection = db["User_Data"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Authenticate user and retrieve user data from MongoDB
def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if not user or not pwd_context.verify(password, user["hashed_password"]):
        return None
    return user


# Create JWT access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# OAuth2PasswordBearer for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency to verify token and get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = users_collection.find_one({"username": username})
    if user is None:
        raise credentials_exception
    return user


# Route to generate access token (Login)
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    # Redirect to home page after successful login
    response = RedirectResponse(url="/")
    response.set_cookie("access_token", access_token)
    response.set_cookie("login_message", "Login successful!")
    return response


# Route to register a new user
@app.post("/register")
async def register(
    username: str = Form(...), password: str = Form(...), email: str = Form(...)
):
    hashed_password = pwd_context.hash(password)
    new_user = {
        "username": username,
        "hashed_password": hashed_password,
        "email": email,
        "role": "user",  # Assign default role for new users
    }
    result = users_collection.insert_one(new_user)
    if result.inserted_id:
        # User registration successful
        message = "User registered successfully!"
        response = RedirectResponse(url="/")
    else:
        # Registration failed
        message = "Registration failed. Please try again."
        response = RedirectResponse(
            url="/register"
        )  # Redirect back to registration page on failure

    # Redirect to home page after registration with message
    response.set_cookie("registration_message", message)
    return response


# Protected route example (requires authentication)
@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "Access granted to protected route"}


### END USER AUTHENTICAION


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
