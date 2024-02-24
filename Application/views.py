from django.shortcuts import render
from . import serializers
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model 
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
# Create your views here.
class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer

#creating user with password

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = serializers.RegisteredUserSerializer

class TenthView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.TenthSerializer


class TwelfthView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.TwelfthSerializer


class CollegeView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.CollegeSerializer

class CollegeDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.CollegeDetailsSerializer

class SchoolingDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.SchoolingDetailsSerializer

class BasicDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.BasicDetailsSerializer

class ResumeView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.ResumeSerializer