from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from api.serializers import UserSerializer, UserSerializerPassWdPost

User = get_user_model()

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = UserSerializer
            return serializer_class
        elif self.request.method == 'POST':
            serializer_class =  UserSerializerPassWdPost
            return serializer_class
        else:
            serializer_class = UserSerializer
            return serializer_class

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer