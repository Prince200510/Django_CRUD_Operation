from rest_framework import generics
from .models import User
from .serializer import UserSerializers

class UserGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers