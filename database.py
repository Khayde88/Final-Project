import pymongo

myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["grocery_db"]
mycol = mydb["SavedList"]

mydict = {
  "date": "1/25/2023",
  "stores": ["wewewe", "Whole Foods Market", "Fareway"],
  "location": "Des Moines, Iowa"
}


x = mycol.insert_one(mydict)