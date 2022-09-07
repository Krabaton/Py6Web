import argparse
import sys
from functools import wraps

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.test

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class ExceptionValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptionValidation(f'Вхідні данні не валідні: {func.__name__}{args}')
        result = func(*args)
        return result

    return wrapper


def find_by_id(_id):
    result = db.cats.find_one({"_id": ObjectId(_id)})
    return result


@validate
def create(name, age, features):
    result = db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    return find_by_id(result.inserted_id)


@validate
def find():
    return db.cats.find()


@validate
def update(_id, name, age, features):
    r = db.cats.update_one({"_id": ObjectId(_id)}, {
        "$set": {
            "name": name,
            "age": age,
            "features": features
        }
    })
    print(r)
    return find_by_id(_id)


@validate
def remove(_id):
    r = db.cats.delete_one({"_id": ObjectId(_id)})
    return r


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                print(r)
            case 'find':
                r = find()
                [print(el) for el in r]
            case 'update':
                r = update(_id, name, age, features)
                print(r)
            case 'remove':
                r = remove(_id)
                print(r)
            case _:
                print('Unknowns command')
    except ExceptionValidation as err:
        print(err)


if __name__ == '__main__':
    main()
    # print(find_by_id('6318d73f74bc292c95cdaa3d'))
