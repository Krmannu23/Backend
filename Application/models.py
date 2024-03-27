from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import random

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

#https://docs.djangoproject.com/en/5.0/topics/db/models/

#while naming model don not put s at last if we use BasicDetails then BasicDetailss table wil create in admin
class BasicDetail(models.Model):
    
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
    titles=models.CharField(max_length=30 ,choices=titlesOptions,null=True)
    firstName=models.CharField(max_length=30,null=True)
    middleName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    dateOfBirth=models.DateField(null=True)
    age=models.CharField(max_length=30,null=True)
    gender=models.CharField(max_length=30,null=True)
    insertDate=models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table='Basic' #This will remove Applicarion name Application.BasicDetails change to only Basic

class ParentDetail(models.Model):
    titlesOptions =[
    ("M01", "Mrs"),
    ("M02", "Miss"),
    ("M03", "Mr"),
    ("D01", "Dr")

    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)
    titles=models.CharField(max_length=30 ,choices=titlesOptions,null=True)
    firstName=models.CharField(max_length=30,null=True)
    middleName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    relationship=models.CharField(max_length=30,null=True)#jaha foreign key use hua wuska sinle father hoga ,child ka details bharne ke liye father table ka details ho chahiye
    insertDate=models.DateTimeField(auto_now_add=True,null=True)
    

    class Meta:
        db_table='Parent'

class Address(models.Model):
   
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id
    adressLine1=models.CharField(max_length=30,null=True)
    addressLine2=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    pincode=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    country=models.CharField(max_length=30,null=True)
    insertDate=models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table='Address'

class AdditionalDetail(models.Model):
    telephoneCodes=[
        ("+91","IND"),
        ("+1","US"),
        ("+27","SA"),
        ("+44","UK"),
        ("+61","AUS")
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id
    telephoneCode=models.CharField(choices=telephoneCodes ,max_length=12,null=True)
    contactNumber=models.PositiveIntegerField(null=True)
    emailId=models.EmailField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    insertDate=models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table='Additional'
    

class Tenth(models.Model):
    tenth_id= models.CharField(max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id

    class Meta:
        db_table='Tenth'

class Twelfth(models.Model):
    twelfth_id= models.CharField(max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id

    class Meta:
        db_table='Twelfth'


    class Meta:
        db_table='College'
class TenSchoolingDetail(models.Model):
    #TenSchoolingDetails ko update karne ke liye tenth_reference ,reference_number pass karna hoga request body me
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE) #request body me pass karna yah id
    tenthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True)
    schoolName=models.CharField(max_length=30,null=True)
    boardName=models.CharField(max_length=30,null=True)
    dateOfEnrollment=models.CharField(max_length=30,null=True)
    insertDate=models.DateTimeField(auto_now_add=True,null=True)
    yearOfPassing=models.CharField(max_length=30,null=True)
    tenth_reference=models.ForeignKey(Tenth,on_delete=models.CASCADE ,related_name="tenth")

    class Meta:
        db_table='TenSchoolingDetail'

class TwelfthSchoolingDetail(models.Model):
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id ,auto generated
    twelfthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True)
    schoolName=models.CharField(max_length=30,null=True)
    boardName=models.CharField(max_length=30,null=True)
    dateOfEnrollment=models.CharField(max_length=30,null=True)
    insertDate=models.DateTimeField(auto_now_add=True,null=True)
    yearOfPassing=models.CharField(max_length=30,null=True)
    twelfth_refrence=models.ForeignKey(Twelfth ,on_delete=models.CASCADE ,related_name="twelfth")

    class Meta:
        db_table='TwelfthSchoolingDetail'


class College(models.Model):
    year = [
    ("YO1", "FIRST"),
    ("YO2", "SECOND"),
    ("YO3", "THIRD"),
    ("YO4", "FOURTH"),
    ("YO5", "FIFTH"),
    ("YO6", "SIXTH"),
    ("YO7", "SEVEN"),
    ]
    college_id= models.CharField(max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)#optinal in request body,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id
    semesterYear=models.CharField(max_length=30,choices=year,null=True)
    
class CollegeDetail(models.Model):
    collegeRollNo=models.PositiveIntegerField(blank=False ,primary_key=True)
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id
    collegeName=models.CharField(max_length=30,null=True)
    universityName=models.CharField(max_length=30,null=True)
    dateOfEnrollment=models.CharField(max_length=30,null=True)
    insertDate=models.DateTimeField(auto_now_add=True)
    yearOfPassing=models.CharField(max_length=30,null=True)
    academicYear=models.ManyToManyField(College)
    class Meta:
        db_table="CollegeDetail"
class Matriculation(models.Model):
    matriculation_Id=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True)
    tenth_reference= models.ForeignKey(Tenth, on_delete=models.CASCADE, related_name='matriculation')
    subjectName = models.CharField(max_length=100,null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    subjectCode = models.CharField(max_length=100,null=True)

    class Meta:
        db_table="Matriculation"

class Intermediate(models.Model):
    intermediateId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True) 
    twelfth_reference= models.ForeignKey(Twelfth, on_delete=models.CASCADE ,related_name='intermediate')
    subjectName = models.CharField(max_length=100,null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    subjectCode = models.CharField(max_length=100,null=True)

    class Meta:
        db_table="Intermediate"

class Semester(models.Model):
    sem = [
    ("SEM1", "SEMESTER 1"),
    ("SEM2", "SEMESTER 2"),
    ("SEM3", "SEMESTER 3"),
    ("SEM4", "SEMESTER 4"),
    ("SEM5", "SEMESTER 5"),
    ("SEM6", "SEMESTER 6"),
    ("SEM7", "SEMESTER 7"),
    ("SEM8", "SEMESTER 8")
    ]
    semesterId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True) 
    semesterNumber=models.CharField(max_length=100 ,choices=sem,null=True)
    college_reference = models.ForeignKey(College,on_delete=models.CASCADE, related_name='semester')#father dependent i.e College

    class Meta:
        db_table="Semester"
class SemesterSubject(models.Model):
    semesterSubjectId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True) 
    subjectName = models.CharField(max_length=100,null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    subjectCode = models.CharField(max_length=100, null=True )
    updatedDate=models.DateTimeField(auto_now_add=True,null=True)
    isUpdated=models.BooleanField(default=False,null=True)
    semester_reference = models.ForeignKey(Semester,on_delete=models.CASCADE, related_name='semesterSubject')#father dependent i.e SEMESTER

    class Meta:
        db_table="SemesterSubject"

class Summary(models.Model):
    summaryId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True) #optinal in request body ,auto generated
    reference_number=models.ForeignKey(BasicDetail,on_delete=models.CASCADE)#request body me pass karna yah id
    matricPercentage=models.FloatField(null=True)
    interPercentage=models.FloatField(null=True)
    graduationPercentage=models.FloatField(null=True)

    class Meta:
        db_table="Summary"
    
class ResponseObjectStudent(models.Model):
    responseId=models.CharField(primary_key=True, default=create_new_ref_number,)
    reference_number=models.OneToOneField(BasicDetail ,on_delete=models.CASCADE)
    class Meta:
        db_table="ResponseObject"
class Navigation(models.Model):
    navigationId=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number,
           primary_key=True) 
    path=models.JSONField(null=True)
    reference_number=models.ForeignKey(BasicDetail ,on_delete=models.CASCADE)