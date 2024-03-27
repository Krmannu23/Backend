from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model

class MatriculationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Matriculation
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.subjectName = validated_data.get('subjectName', instance.subjectName)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.subjectCode = validated_data.get('subjectCode', instance.subjectCode)
        instance.save()
        return instance
class IntermediateSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Intermediate
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.subjectName = validated_data.get('subjectName', instance.subjectName)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.subjectCode = validated_data.get('subjectCode', instance.subjectCode)
        instance.save()
        return instance

class SemsterSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.SemesterSubject
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.subjectName = validated_data.get('subjectName', instance.subjectName)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.subjectCode = validated_data.get('subjectCode', instance.subjectCode)
        instance.updatedDate=validated_data.get('updatedDate', instance.updatedDate)
        instance.isUpdated=validated_data.get('isUpdated', instance.isUpdated)
        instance.save()
        return instance
class SemsterSerializer(serializers.ModelSerializer):
   semesterSubject=SemsterSubjectSerializer(many=True)
   class Meta:
        model=models.Semester
        fields='__all__'
   def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.semesterNumber = validated_data.get('semesterNumber', instance.semesterNumber)
        instance.save()
        return instance

class AdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalDetail
        fields='__all__'

class TenthSerializer(serializers.ModelSerializer):
    matriculation=MatriculationSerializer(many=True)
    
  
   
    class Meta:
        model=models.Tenth
        fields='__all__'
    
class TwelfthSerializer(serializers.ModelSerializer):
    intermediate=IntermediateSerializer(many=True)
    class Meta:
        model=models.Twelfth
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    semester=SemsterSerializer(many=True)
    class Meta:
        model=models.College
        fields='__all__'

    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.semesterYear = validated_data.get('semesterYear', instance.semesterYear)
        instance.save()
        return instance

class CollegeDetailsSerializer(serializers.ModelSerializer):
    academicYear=CollegeSerializer(many=True)# since  models of  CollegeDetailsSerializer and CollegeSerializer not linked ,name of serializer can be anything
    class Meta:
        model=models.CollegeDetail
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.collegeRollNo = validated_data.get('collegeRollNo', instance.collegeRollNo)
        instance.collegeName = validated_data.get('collegeName', instance.collegeName)
        instance.universityName = validated_data.get('universityName', instance.universityName)
        instance.dateOfEnrollment = validated_data.get('dateOfEnrollment', instance.dateOfEnrollment)
        instance.insertDate = validated_data.get('insertDate', instance.insertDate)
        instance.yearOfPassing = validated_data.get('yearOfPassing', instance.yearOfPassing)
        instance.save()
        return instance
class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Summary
        fields='__all__'

    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
        instance.graduationPercentage= validated_data.get('graduationPercentage', instance.graduationPercentage)
        instance.matricPercentage= validated_data.get('matricPercentage', instance.matricPercentage)
        instance.interPercentage= validated_data.get('interPercentage', instance.interPercentage)
        instance.save()
        return instance

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
        model = models.ParentDetail
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.titles = validated_data.get('titles', instance.titles)
        instance.adressLine1 = validated_data.get('adressLine1', instance.adressLine1)
        instance.addressLine2 = validated_data.get('addressLine2', instance.addressLine2)
        instance.city = validated_data.get('city', instance.city)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country 
                                              )
        instance.save()
        return instance

class TenSchoolingDetailsSerializer(serializers.ModelSerializer):
   # since  models of  TenSchoolingDetailsSerializer and TenthSerializer is linked ,name of serializer cannot be anything

    tenth_reference=TenthSerializer(many=False)#tenth_reference TenSchoolingDetails model me hona chahiye
    class Meta:
        model = models.TenSchoolingDetail
        fields='__all__'
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
        
        #attributename that you want to update
        instance.schoolName= validated_data.get('schoolName', instance.schoolName)
        instance.boardName= validated_data.get('boardName', instance.boardName)
        instance.dateOfEnrollment= validated_data.get('dateOfEnrollment', instance.dateOfEnrollment)
        instance.yearOfPassing= validated_data.get('yearOfPassing', instance.yearOfPassing)
        #instance.tenth_reference.matriculation.subjectName= validated_data.get('tenth_reference', {}).get('matriculation',{}).get('subjectName')
        # for element in validated_data.get('tenth_reference', {}).get('matriculation',[]):
        #     print(element)
        #     print("\n")
            #instance.tenth_reference.matriculation.add(dict(element))
            #print(instance.tenth_reference.matriculation)
        instance.tenthRollNo= validated_data.get('tenthRollNo', instance.tenthRollNo)
        instance.save()
        return instance
   
   
class TwelfthSchoolingDetailsSerializer(serializers.ModelSerializer):
    twelfth_refrence=TwelfthSerializer(many=False)#twelfth_refrence TwelfthSchoolingDetails  model me hona chaiye
    class Meta:
        model = models.TwelfthSchoolingDetail
        fields='__all__'
    
    def update(self,instance ,validated_data):#validate_data is request body and instance is attribute of model
      
        instance.twelfthRollNo = validated_data.get('twelfthRollNo', instance.twelfthRollNo)
        instance.schoolName = validated_data.get('schoolName', instance.schoolName)
        instance.boardName = validated_data.get('twelfthRollNo', instance.boardName)
        instance.dateOfEnrollment = validated_data.get('dateOfEnrollment', instance.dateOfEnrollment)
        instance.yearOfPassing= validated_data.get('yearOfPassing', instance.yearOfPassing)
        instance.save()
        return instance
class BasicDetailsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=models.BasicDetail
        fields="__all__"

class ResponsePayloadSeializer(serializers.ModelSerializer):
    class Meta:
        model=models.ResponseObjectStudent
        fields="__all__"
class NavigationSeializer(serializers.ModelSerializer):
    class Meta:
        model=models.Navigation
        fields="__all__"
