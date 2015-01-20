from mongoengine import *
connect('simplisafe')

class User(Document):
    name = StringField()
    password = StringField()
    uid = StringField()
    token = StringField()
    cookies = StringField()
    meta = {"db_alias": "user-db"}

class Location(Document):
    lid = StringField()



