from django.db import models

# Create your models here.
# accounts/models.py

from django.db import models

class User(models.Model):
   
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # In a real project, use a password hash

class UserData(models.Model):
    username = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    def __str__(self):
        return "Email: "+self.username + "----Password: "+self.key