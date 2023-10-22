from django.db import models

# Create your models here.

class inbox(models.Model):
    message_no = models.CharField(unique=True,max_length=10)
    sender = models.CharField(default="", max_length=50)
    reciever = models.CharField(default="", max_length=50)
    date = models.CharField(default="", max_length=100)
    subject = models.CharField(default="", max_length=100)
    category = models.CharField(default="",max_length = 100)
    content = models.CharField(default="", max_length=10000)


