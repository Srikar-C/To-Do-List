from django.db import models

# Create your models here.


class UserDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Items(models.Model):
    user_list = models.ForeignKey(UserDetails,on_delete= models.CASCADE)
    list = models.CharField(max_length=255)