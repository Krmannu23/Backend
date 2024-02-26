from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Subject
        exclude=['subjectId']


class AdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherDetails
        exclude=['idNumber']
class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Name
        fields="__all__"

class TenthSerializer(serializers.ModelSerializer):
    subject=SubjectSerializer(many=True)
    class Meta:
        model=models.Tenth
        exclude=['tenId']

class TwelfthSerializer(serializers.ModelSerializer):
    subject=SubjectSerializer(many=True)
    class Meta:
        model=models.Twelfth
        exclude=['twelfthId']

class CollegeSerializer(serializers.ModelSerializer):
    subject=SubjectSerializer(many=True)
    class Meta:
        model=models.College
        exclude=['collegeId']

class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CollegeDetails
        fields='__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Summary
        exclude=['summaryId']
class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id', 'username','password', 'first_name', 'last_name')

UserModel = get_user_model()
class RegisteredUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            firstName=validated_data['first_name'],
            lastName=validated_data['last_name'],
            email=validated_data['email'],
            #gender=validated_data['gender'], if go Inside User model only username ,password,email,first_name ,last_name h isliye or koi aur field nhi lega
        )

        return user

    class Meta:
        model = UserModel

        fields = ( "id", "username", "password", "email","firstName","lastName") #( "id", "username", "password", "email","gender")

class ParentDetailsSerializer(serializers.ModelSerializer):
    parent=NameSerializer()
    otherDetails=AdditionalDetailsSerializer()
    class Meta:
        model = models.ParentDetails
        exclude=['parentId']



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude=['addressId']

class TenSchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TenSchoolingDetails
        exclude=['tenthRollNo']

class TwelfthSchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TwelfthSchoolingDetails
        exclude=['twelfthRollNo']

class BasicDetailsSerializer(serializers.ModelSerializer):
    name=NameSerializer()
    otherDetails=AdditionalDetailsSerializer()
    parentInfo=ParentDetailsSerializer()
   
    class Meta:
        model=models.BasicDetails
        fields="__all__"
class FullApiSerializer(serializers.ModelSerializer):
    basicDetails = BasicDetailsSerializer()
    tenthSchoolingDetails = TenSchoolingDetailsSerializer()
    twelfthSchoolingDetails = TwelfthSchoolingDetailsSerializer()
    collegeDetails = CollegeDetailsSerializer()
    tenth = TenthSerializer()
    twelfth = TwelfthSerializer()
    college = CollegeSerializer()
    studentSummary=SummarySerializer()

    class Meta:
        model = models.FullApi
        fields='__all__'