from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        models=models.Subject
        fields='__all__'
class TenthSerializer(serializers.ModelSerializer):
    subject_name=SubjectSerializer(many=True)
    class Meta:
        model=models.Tenth
        fields='__all__'

class TwelfthSerializer(serializers.ModelSerializer):
    subject_name=SubjectSerializer(many=True)
    class Meta:
        model=models.Twelfth
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    subject_name=SubjectSerializer(many=True)
    class Meta:
        model=models.College
        fields='__all__'


class BasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BasicDetails
        fields='__all__'



class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CollegeDetails
        fields='__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Resume
        fields='__all__'
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
        fields = '__all__'

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Name
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

class TenSchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TenSchoolingDetails
        fields = '__all__'

class TwelfthSchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TwelfthSchoolingDetails
        fields = '__all__'
class FullApiSerializer(serializers.ModelSerializer):
    basic_details = BasicDetailsSerializer()
    parent_details = ParentDetailsSerializer()
    name = NameSerializer()
    address = AddressSerializer()
    #resume = ResumeSerializer()
    tenth_schooling_details = TenSchoolingDetailsSerializer()
    twelfth_schooling_details = TwelfthSchoolingDetailsSerializer()
    college_details = CollegeDetailsSerializer()
    tenth = TenthSerializer()
    twelfth = TwelfthSerializer()
    college = CollegeSerializer()

    class Meta:
        model = models.FullApi
        fields = '__all__'