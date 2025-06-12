from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializers
from rest_framework.views import APIView 
from django.shortcuts import get_object_or_404

class UserAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializers = UserSerializers(user, many = True)
        return Response(serializers.data)
        
class UserOperation(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk = pk)
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)