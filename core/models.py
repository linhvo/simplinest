from mongoengine import *
import datetime

class User(Document):
    nest_access_token = StringField()
    nest_status = StringField()
    datetime = DateTimeField(default=datetime.datetime.now())

class Location(Document):
    lid = StringField()

class NestAuth(Document):
    access_token = StringField()
    expiration = DateTimeField()
    client_id = StringField()
    client_secret = StringField()
    auth_code = StringField()





