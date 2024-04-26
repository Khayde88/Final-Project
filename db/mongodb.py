from pymongo import MongoClient

uri = ""

client = MongoClient("mongodb://localhost:27017/")
db = client["grocery_db"]
collection = db["grocery_items"]


def add_grocery(item_data: dict):
    result = collection.insert_one(item_data)
    return result


def get_groceries():
    groceries = list(collection.find({}))
    return groceries
