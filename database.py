import pymongo

myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["grocery_db"]
mycol = mydb["SavedList"]

mydict = {
  "date": "1/15/2023",
  "stores": ["Target", "Whole Foods Market", "Fareway"],
  "location": "Noahs Second Test, Iowa"
}


x = mycol.insert_one(mydict)