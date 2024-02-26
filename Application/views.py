from django.shortcuts import render
from . import serializers
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model 
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .import models
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
    queryset = models.Tenth.objects.all()
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

class TenSchoolingDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.TenSchoolingDetailsSerializer
class TwelfthSchoolingDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.TwelfthSchoolingDetailsSerializer

class BasicDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.BasicDetailsSerializer

class SummaryView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.SummarySerializer

class FullApiView(CreateAPIView):
    permission_class=permissions.AllowAny
    serializer_class=serializers.FullApiSerializer