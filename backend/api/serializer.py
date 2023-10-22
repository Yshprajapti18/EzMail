from rest_framework import serializers
from .models import inbox

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=inbox
        fields=('message_no','sender','reciever','date','subject','category','content')
