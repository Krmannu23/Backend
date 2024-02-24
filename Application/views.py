from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets, permissions
# Create your views here.

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