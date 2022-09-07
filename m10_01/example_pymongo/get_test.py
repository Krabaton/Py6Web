from pymongo import MongoClient

client = MongoClient("mongodb+srv://goitlearn:<password>@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

r = db.cats.find({})

for c in r:
    print(c)
