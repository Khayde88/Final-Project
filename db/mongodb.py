from pymongo import MongoClient

uri = "mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)


db = client["grocery_db"]
collection = db["grocery_items"]


def add_grocery(item_data: dict):
    result = collection.insert_one(item_data)
    return result


def get_groceries():
    groceries = list(collection.find({}))
    return groceries
