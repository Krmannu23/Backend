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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#creating user with password

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = serializers.RegisteredUserSerializer

class TenthView(viewsets.ModelViewSet):
    queryset = models.Tenth.objects.all()
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TenthSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TwelfthView(viewsets.ModelViewSet):
    queryset=models.Twelfth.objects.all()
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TwelfthSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CollegeView(viewsets.ModelViewSet):
    queryset=models.College.objects.all()
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.CollegeSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CollegeDetailsView(viewsets.ModelViewSet):
    queryset=models.CollegeDetails.objects.all()
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.CollegeDetailsSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TenSchoolingDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TenSchoolingDetailsSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class TwelfthSchoolingDetailsView(viewsets.ModelViewSet):
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TwelfthSchoolingDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BasicDetailsView(viewsets.ModelViewSet):
    queryset=models.BasicDetails.objects.all()
    permission_class=permissions.IsAuthenticated
    serializer_class=serializers.BasicDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SummaryView(viewsets.ModelViewSet):
    permission_class=permissions.AllowAny
    serializer_class=serializers.SummarySerializer

class FullApiView(CreateAPIView):
    permission_class=permissions.AllowAny
    serializer_class=serializers.FullApiSerializer