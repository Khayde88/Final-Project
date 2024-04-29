import pymongo

myclient = pymongo.MongoClient("mongodb+srv://canderson32:Kotaikanaxai_88@cluster0.dswl3pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["grocery_db"]
mycol = mydb["grocery_items"]

mydict = {
  "name": "Vitamin D Whole Milk",
  "price": 5.09,
  "category": "Dairy & Eggs",
  "brand": "Hy-Vee",
  "quantity": "1 gal",
  "image": "https://api.hy-vee.cloud/cdn-cgi/image/f=auto,w=828,q=60,dpr=1/https://e22d0640933e3c7f8c86-34aee0c49088be50e3ac6555f6c963fb.ssl.cf2.rackcdn.com/0075450097000_CL_Syndigo_default_large.png"
}


x = mycol.insert_one(mydict)