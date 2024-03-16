from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model

class MatriculationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Matriculation
        fields='__all__'

class IntermediateSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Intermediate
        fields='__all__'


class SemsterSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.SemesterSubject
        fields='__all__'
class SemsterSerializer(serializers.ModelSerializer):
   subject=SemsterSubjectSerializer(many=True)
   class Meta:
        model=models.Semester
        fields='__all__'

class AdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalDetails
        fields='__all__'

class TenthSerializer(serializers.ModelSerializer):
    subject=MatriculationSerializer(many=True)
    class Meta:
        model=models.Tenth
        fields='__all__'

class TwelfthSerializer(serializers.ModelSerializer):
    subject=IntermediateSerializer(many=True)
    class Meta:
        model=models.Twelfth
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    semester=SemsterSerializer(many=True)
    class Meta:
        model=models.College
        fields='__all__'

class CollegeDetailsSerializer(serializers.ModelSerializer):
    college=CollegeSerializer(many=False)
    class Meta:
        model=models.CollegeDetails
        fields='__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Summary
        fields='__all__'
class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id', 'username','password', 'first_name', 'last_name')

UserModel = get_user_model()
class RegisteredUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
#Exception Value:	 Field name `firstName` is not valid for model `User`.
        # user = UserModel.objects.create_user(
        #     username=validated_data['username'],
        #     password=validated_data['password'],
        #     firstName=validated_data['first_name'],
        #     lastName=validated_data['last_name'],
        #     email=validated_data['email'],
        #     #gender=validated_data['gender'], if go Inside User model only username ,password,email,first_name ,last_name h isliye or koi aur field nhi lega
        # )
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            #gender=validated_data['gender'], if go Inside User model only username ,password,email,first_name ,last_name h isliye or koi aur field nhi lega
        )

        return user

    class Meta:
        model = UserModel

        fields = ( "id", "username", "password", "email","first_name","last_name") #( "id", "username", "password", "email","gender")

class ParentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParentDetails
        fields='__all__'



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields='__all__'

class TenSchoolingDetailsSerializer(serializers.ModelSerializer):
    tenth=TenthSerializer(many=False)
    class Meta:
        model = models.TenSchoolingDetails
        fields='__all__'

class TwelfthSchoolingDetailsSerializer(serializers.ModelSerializer):
    twelfth=TwelfthSerializer(many=False)
    class Meta:
        model = models.TwelfthSchoolingDetails
        fields='__all__'
class BasicDetailsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=models.BasicDetails
        fields="__all__"

class StudentDetailsSerializer(serializers.ModelSerializer):
    basicDetails=BasicDetailsSerializer()
    parent=ParentDetailsSerializer(many=False)
    address=AddressSerializer(many=False)
    additionalDetails=AdditionalDetailsSerializer(many=False)
    
    class Meta:
        model=models.StudentDetails
        fields="__all__"
class ResponsePayload(serializers.ModelSerializer):
    studentDetails=StudentDetailsSerializer()
    tenthDetails=TenSchoolingDetailsSerializer()
    twelfthDetails=TwelfthSchoolingDetailsSerializer()
    collegeDetails=CollegeDetailsSerializer()
    summary=SummarySerializer()
    class Meta:
        model=models.ResponseObjectStudent
        fields="__all__"