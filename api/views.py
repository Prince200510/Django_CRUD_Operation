from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializers

# @api_view(['GET'])
# def get_user(request):
#     return Response(UserSerializers({'name' : 'Prince Maurya', 'age' : 20}).data)

@api_view(['GET'])
def get_user(request):
    user = User.objects.all()
    serializer = UserSerializers(user, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializers(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        