from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import inbox
from .serializer import DataSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def getData(request,*args, **kwargs):
    app = inbox.objects.all()
    serializer = DataSerializer(app,many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def putData(request,*args, **kwargs):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)