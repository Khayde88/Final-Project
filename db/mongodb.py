from pymongo import MongoClient

# MongoDB Atlas URI
uri = "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client (client will be created in main.py)
client = None


def initialize_mongodb():
    global client
    client = MongoClient(uri)


def add_grocery(item_data: dict):
    db = client["grocery_db"]
    collection = db["grocery_items"]
    result = collection.insert_one(item_data)
    return result


def get_groceries():
    db = client["grocery_db"]
    collection = db["grocery_items"]
    groceries = list(collection.find({}))
    return groceries
