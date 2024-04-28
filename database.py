import pymongo

myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["grocery_db"]
mycol = mydb["SavedList"]

mydict = {
  "date": "6/24/2023",
  "stores": ["Aldis", "Walmart", "Costco"],
  "location": "Des Moines, Iowa"
}


x = mycol.insert_one(mydict)