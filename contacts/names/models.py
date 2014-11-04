from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=30)