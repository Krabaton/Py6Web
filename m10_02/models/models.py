from mongoengine import *

connect(host='mongodb://localhost:27017/test')


class Contacts(Document):
    first_name = StringField(max_length=120, min_length=1, required=True)
    last_name = StringField(max_length=120, min_length=1, required=False)
    age = IntField(min_value=21, max_value=75, required=True)
    email = StringField(required=True)
    cell_phone = StringField(required=False)
    completed = BooleanField(default=False)
