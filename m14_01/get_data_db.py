from pymongo import MongoClient

client = MongoClient("mongodb+srv://*******:*******@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority")

db = client["web6"]

if __name__ == '__main__':
    r = db.losses.find(sort=[('date', -1)])
    for el in r:
        print(el)