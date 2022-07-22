from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db:27017/app")
db = client.app


@app.route('/')
def index():
    result = {}
    cursor = db.users.find({})
    for el in cursor:
        result.update({"name": el.get('name')})
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
