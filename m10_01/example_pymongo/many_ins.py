from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.test

db.cats.insert_many([
  {
    "name": 'Lama',
    "age": 2,
    "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
  },
  {
    "name": 'Liza',
    "age": 4,
    "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
  },
])
