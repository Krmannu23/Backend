from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import random

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

#https://docs.djangoproject.com/en/5.0/topics/db/models/

class BasicDetails(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reference_number = models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True
      )
    titlesOptions =[
    ("M01", "Mrs"),
    ("M02", "Miss"),
    ("M03", "Mr"),
    ("D01", "Dr")
    ]
    titles=models.CharField(max_length=30 ,choices=titlesOptions)
    firstName=models.CharField(max_length=30)
    middleName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    dateOfBirth=models.DateField()
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)

class ParentDetails(models.Model):
    titlesOptions =[
    ("M01", "Mrs"),
    ("M02", "Miss"),
    ("M03", "Mr"),
    ("D01", "Dr")
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    titles=models.CharField(max_length=30 ,choices=titlesOptions)
    firstName=models.CharField(max_length=30)
    middleName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    relationship=models.CharField(max_length=30)#jaha foreign key use hua wuska sinle father hoga ,child ka details bharne ke liye father table ka details ho chahiye
    timestamp=models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    adressLine1=models.CharField(max_length=30)
    addressLine2=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)

class OtherDetails(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    contactNumber=models.PositiveIntegerField()
    emailId=models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    

class Tenth(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    timestamp=models.DateTimeField(auto_now_add=True)


class Twelfth(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    timestamp=models.DateTimeField(auto_now_add=True)

class College(models.Model):
    sem = [
    ("SEM1", "SEMSTER 1"),
    ("SEM2", "SEMSTER 2"),
    ("SEM3", "SEMSTER 3"),
    ("SEM4", "SEMSTER 4"),
    ("SEM5", "SEMSTER 5"),
    ("SEM6", "SEMSTER 6"),
    ("SEM7", "SEMSTER 7"),
    ("SEM8", "SEMSTER 8")
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    seamster=models.CharField(max_length=30,choices=sem)
    timestamp=models.DateTimeField(auto_now_add=True)
class TenSchoolingDetails(models.Model):
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE) #request body me pass karna yah id
    tenthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Matriculation roll number cannot be empty'})
    schoolName=models.CharField(max_length=30)
    boardName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    yearOfPassing=models.CharField()
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)


class TwelfthSchoolingDetails(models.Model):
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id ,auto generated
    twelfthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Inter roll number cannot be empty'})
    schoolName=models.CharField(max_length=30)
    boardName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    yearOfPassing=models.CharField()
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
class CollegeDetails(models.Model):
    collegeRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'College roll number cannot be empty'})
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    collegeName=models.CharField(max_length=30)
    universityName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)


class Matriculation(models.Model):
    subjectId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)
    reference_number = models.ForeignKey(Tenth, on_delete=models.CASCADE, related_name='Matriculation')
    subjectName = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    subjectCode = models.CharField(max_length=100)

class Intermediate(models.Model):
    subjectId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)
    reference_number = models.ForeignKey(Twelfth, on_delete=models.CASCADE, related_name='Intermediate')
    subjectName = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    subjectCode = models.CharField(max_length=100)

class Semester(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    semester=models.CharField(max_length=100)
    reference_number = models.ForeignKey(College,on_delete=models.CASCADE, related_name='semster')#father dependent i.e College
class SemesterSubject(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    subjectName = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    subjectCode = models.CharField(max_length=100)
    reference_number = models.ForeignKey(Semester,on_delete=models.CASCADE, related_name='semesterSubject')#father dependent i.e Semster

class Summary(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body ,auto generated
    reference_number=models.ForeignKey(BasicDetails,on_delete=models.CASCADE)#request body me pass karna yah id
    matricPercentage=models.FloatField()
    interPercentage=models.FloatField()
    graduationPercentage=models.FloatField()
    
class ResponseObjectStudent(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)

