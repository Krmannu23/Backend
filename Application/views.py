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
    queryset=models.CollegeDetail.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.CollegeDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.CollegeDetail.objects.all()))>0:
            instance = models.CollegeDetail.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   

class TenSchoolingDetailsView(viewsets.ModelViewSet):
    queryset=models.TenSchoolingDetail.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TenSchoolingDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.TenSchoolingDetail.objects.all()))>0:
            instance = models.TenSchoolingDetail.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    
   
class TwelfthSchoolingDetailsView(viewsets.ModelViewSet):
    queryset=models.TwelfthSchoolingDetail.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.TwelfthSchoolingDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.TwelfthSchoolingDetail.objects.all()))>0:
            instance = models.TwelfthSchoolingDetail.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

# WE CAN UPDATE THE DATA USING ONLY VIEW OR USING ONLY SERIALIZER OR USING both ,for nested serializer we need update method in serializer
class BasicDetailsView(viewsets.ModelViewSet):
    queryset=models.BasicDetail.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.BasicDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.BasicDetail.objects.all()))>0:
            instance = models.BasicDetail.objects.get(reference_number=key)
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
    queryset=models.AdditionalDetail.objects.all()
    # permission_class=permissions.IsAuthenticated
    serializer_class=serializers.AdditionalDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and len(list(models.AdditionalDetail.objects.all())):
            instance = models.AdditionalDetail.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   
    

class ParentDetailsView(viewsets.ModelViewSet):
    queryset = models.ParentDetail.objects.all()
    serializer_class = serializers.ParentDetailsSerializer
    lookup_field = 'reference_number'

    def create(self, request, *args, **kwargs):
        #print(request.data.get('reference_number')) giving key ,and There is no ParentDetails created ,so we will get 
        #DoesNotExist at /application/user/details/parent 
        key = request.data.get('reference_number') 
        if len(list(models.ParentDetail.objects.all())) > 0 and key:
            instance = models.ParentDetail.objects.get(reference_number=key)
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
    serializer_class=serializers.ResponsePayloadSeializer



class MatriculationView(viewsets.ModelViewSet):
    queryset=models.Matriculation.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.MatriculationSerializer

    def create(self, request, *args, **kwargs):
        #below line will not work because same tenth_reference contain by other object
        #key = request.data.get('tenth_reference')#extract tenth_reference from request body
        #subject would be unique for all matriculation object for same tenth_reference
        key = request.data.get('subjectCode')
        #if request.data.get('matriculation_Id'):#we need this check beacuse we know we can update using primary key
        if (request.data.get('matriculation_Id') and key):
            #below line will not work because same tenth_reference contain by other object
            #instance = models.Matriculation.objects.get(tenth_reference=key)
            instance = models.Matriculation.objects.get(subjectCode=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

class IntermediateView(viewsets.ModelViewSet):
    queryset=models.Intermediate.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.IntermediateSerializer

    def create(self, request, *args, **kwargs):
        key = request.data.get('subjectCode')
        if (request.data.get('intermediateId') and key):
            instance = models.Intermediate.objects.get(subjectCode=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

class SemesterSubjectView(viewsets.ModelViewSet):
    queryset=models.SemesterSubject.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.SemsterSubjectSerializer

    def create(self, request, *args, **kwargs):
        key = request.data.get('subjectCode')
        if (request.data.get('semesterSubjectId') and key):
            instance = models.SemesterSubject.objects.get(subjectCode=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class NavigationView(viewsets.ModelViewSet):
    queryset=models.Navigation.objects.all()
    permission_class=permissions.AllowAny
    serializer_class=serializers.NavigationSeializer
#TEST DATA
#    "path": {
#             "key1": "value1",
#             "key2": [
#                 "value1",
#                 "value3"
#             ],
#             "key3": {
#                 "nested_key": "nested_value"
#             }
#         }
#     }
    def create(self, request, *args, **kwargs):
        key = request.data.get('reference_number')
        if key and request.data.get('navigationId'):
            instance = models.Navigation.objects.get(reference_number=key)
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()

   