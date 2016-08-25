from django.db import models


class Location(models.Model):
    lid = models.CharField(max_length=255)


class NestAuth(models.Model):
    access_token = models.CharField(max_length=255)
    expiration = models.DateTimeField(null=True, blank=True)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    auth_code = models.CharField(max_length=255)


class Devices(models.Model):
    structure_id = models.CharField(max_length=255)
    auth = models.ForeignKey(NestAuth, name='nest_auth')
    

class NestUser(models.Model):
    nest_access_token = models.CharField(max_length=255)
    nest_status = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)




