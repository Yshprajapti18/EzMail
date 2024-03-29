from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    sender = models.EmailField()
    recipients = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    tag = models.CharField(max_length=50,default=None)
    timestamp = models.DateTimeField(auto_now_add=True)


    
