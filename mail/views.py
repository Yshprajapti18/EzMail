# Import necessary modules and classes
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import DataSerializer  # Import the serializer class
from .models import Email  # Import the Email model
from rest_framework import status

# Define view functions

# Decorate the function to specify that it handles GET requests
@api_view(['GET'])
def inbox(request,*args,**kwargs):
    # Retrieve all emails from the database
    app = Email.objects.all()
    # Serialize the queryset of emails
    serializer = DataSerializer(app, many=True)
    # Return the serialized data as a response
    return Response(serializer.data)

# Decorate the function to specify that it handles POST requests
@api_view(['POST'])
def send(request,*args,**kwargs):
    # Initialize the serializer with the request data
   
        serializer = DataSerializer(data=request.data)
        # Check if the serializer is valid
        if serializer.is_valid():
            # Save the data from the serializer to the database
            serializer.save()
            # Return the serialized data as a response
            return Response(serializer.data)
        # Return any errors in the serializer as a response with status code 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,id):
    try:
        instance = Email.objects.get(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Email.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    

     
