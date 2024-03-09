from django.shortcuts import render
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, status
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
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TenthSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.Tenth.objects.all()))>0:
            instance = models.Tenth.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()


class TwelfthView(viewsets.ModelViewSet):
    queryset=models.Twelfth.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TwelfthSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.Twelfth.objects.all())>0):
            instance = models.Twelfth.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   


class CollegeView(viewsets.ModelViewSet):
    queryset=models.College.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.CollegeSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key  and len(list(models.College.objects.all()))>0:
            instance = models.College.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   

class CollegeDetailsView(viewsets.ModelViewSet):
    queryset=models.CollegeDetails.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.CollegeDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.CollegeDetails.objects.all()))>0:
            instance = models.CollegeDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   

class TenSchoolingDetailsView(viewsets.ModelViewSet):
    queryset=models.TenSchoolingDetails.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TenSchoolingDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.TenSchoolingDetails.objects.all()))>0:
            instance = models.TenSchoolingDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   
class TwelfthSchoolingDetailsView(viewsets.ModelViewSet):
    queryset=models.TwelfthSchoolingDetails.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TwelfthSchoolingDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.TwelfthSchoolingDetails.objects.all()))>0:
            instance = models.TwelfthSchoolingDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

class BasicDetailsView(viewsets.ModelViewSet):
    queryset=models.BasicDetails.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.BasicDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.BasicDetails.objects.all()))>0:
            instance = models.BasicDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
    

class AddressDetailsView(viewsets.ModelViewSet):
    queryset=models.Address.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.AddressSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.Address.objects.all()))>0:
            instance = models.Address.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
    

class AdditionalDetailsView(viewsets.ModelViewSet):
    queryset=models.OtherDetails.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.AdditionalDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.OtherDetails.objects.all())):
            instance = models.OtherDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    

class ParentDetailsView(viewsets.ModelViewSet):
    queryset = models.ParentDetails.objects.all()
    serializer_class = serializers.ParentDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        #print(request.data.get('reference_number')) giving key ,and There is no ParentDetails created ,so we will get 
        #DoesNotExist at /application/user/details/parent 
        key = request.data.get('reference_number') 
        if len(list(models.ParentDetails.objects.all())) > 0 and key:
            instance = models.ParentDetails.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

    
# In a ModelViewSet, you typically use the lookup_field attribute to specify the field other than the primary key that should be used for retrieving instances. Here's how you can do it:
# Assuming you have a model YourModel with a unique field unique_field:
# python
# Copy code
# from rest_framework import viewsets
# from .models import YourModel
# from .serializers import YourModelSerializer

# class YourModelViewSet(viewsets.ModelViewSet):
#     queryset = YourModel.objects.all()
#     serializer_class = YourModelSerializer
#     lookup_field = 'unique_field'
# In this example, the lookup_field is set to 'unique_field', which means that DRF will use the unique_field instead of the primary key for retrieving instances of YourModel.

# Now, your URLs for retrieving, updating, and deleting instances would look like this:

# GET /your-models/{unique_field}/
# PUT /your-models/{unique_field}/
# PATCH /your-models/{unique_field}/
# DELETE /your-models/{unique_field}/

class SummaryView(viewsets.ModelViewSet):
    queryset=models.Summary.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.SummarySerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.Summary.objects.all()))>0:
            instance = models.Summary.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
class ResponseApi(viewsets.ModelViewSet):
    queryset=models.ResponseObjectStudent.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.ResponsePayload



