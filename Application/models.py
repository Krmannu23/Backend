from django.db import models
from django.contrib.auth.models import User

#https://docs.djangoproject.com/en/5.0/topics/db/models/
#jaha foreign key use hua wuska sinle father hoga ,child ka details bharne ke liye father table ka details ho chahiye
class Subject(models.Model):
    subject = [
    ("MA01", "MATHS"),
    ("PH01", "PHYSCIS"),
    ("ENG01", "ENGLISH"),
    ("SC01", "SCIENCE"),
    ("HI01", "HINDI")
    ]
    subjectId=models.UUIDField(primary_key=True)
    subjectName=models.CharField(choices=subject,max_length=30)
    pointsOrMarks=models.FloatField()

class Name(models.Model):#https://docs.djangoproject.com/en/5.0/ref/models/fields/
    titles_options =[
    ("M01", "Mrs"),
    ("M02", "Miss"),
    ("M03", "Mr"),
    ("D01", "Dr")
    ]
    titles=models.CharField(max_length=30 ,choices=titles_options)
    firstName=models.CharField(max_length=30)
    middleName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)

class Address(models.Model):
    addressId=models.UUIDField(primary_key=True)
    adressLine1=models.CharField(max_length=30)
    addressLine2=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

class OtherDetails(models.Model):
    idNumber=models.CharField(max_length=30,primary_key=True)
    contactNumber=models.PositiveIntegerField()
    emailId=models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    

class Tenth(models.Model):
    tenId=models.UUIDField(primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insertDate=models.DateTimeField()


class Twelfth(models.Model):
    twelfthId=models.UUIDField(primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insertDate=models.DateTimeField()
class College(models.Model):
    collegeId=models.UUIDField(primary_key=True)
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
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insertDate=models.DateTimeField()
    seamster=models.CharField(max_length=30,choices=sem)

class ParentDetails(models.Model):
    parentId=models.UUIDField(primary_key=True)
    parent=models.OneToOneField(Name, on_delete=models.CASCADE)#this parent name also present in Parent serializer ,if different then ,code will get duplicate
    otherDetails=models.OneToOneField(OtherDetails, on_delete=models.CASCADE)
    relationship=models.CharField(max_length=30)
class BasicDetails(models.Model):
    userId=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.OneToOneField(Name, on_delete=models.CASCADE)
    dateOfBirth=models.DateField()
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    otherDetails=models.OneToOneField(OtherDetails, on_delete=models.CASCADE)
    parentInfo=models.OneToOneField(ParentDetails, on_delete=models.CASCADE)
class TenSchoolingDetails(models.Model):
    tenthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Matriculation roll number cannot be empty'})
    schoolName=models.CharField(max_length=30)
    boardName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    yearOfPassing=models.CharField()
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)


class TwelfthSchoolingDetails(models.Model):
    twelfthRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Inter roll number cannot be empty'})
    schoolName=models.CharField(max_length=30)
    boardName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    yearOfPassing=models.CharField()
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)
class CollegeDetails(models.Model):
    collegeName=models.CharField(max_length=30)
    universityName=models.CharField(max_length=30)
    dateOfEnrollment=models.CharField(max_length=30)
    collegeRollNo=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'College roll number cannot be empty'})
    insertDate=models.DateTimeField()
    yearOfPassing=models.CharField(max_length=30)


class Summary(models.Model):
    summaryId=models.UUIDField(primary_key=True)
    matricPercentage=models.FloatField()
    interPercentage=models.FloatField()
    graduationPercentage=models.FloatField()
    
class FullApi(models.Model):
    # jsika jiska me oneToOne h name must be align in serializer also
    basicDetails = models.OneToOneField(BasicDetails, on_delete=models.CASCADE)
    tenthSchoolingDetails = models.OneToOneField(TenSchoolingDetails, on_delete=models.CASCADE)
    twelfthSchoolingDetails = models.OneToOneField(TwelfthSchoolingDetails, on_delete=models.CASCADE)
    collegeDetails = models.OneToOneField(CollegeDetails, on_delete=models.CASCADE)
    tenth = models.OneToOneField(Tenth, on_delete=models.CASCADE)
    twelfth = models.OneToOneField(Twelfth, on_delete=models.CASCADE)
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    studentSummary=models.OneToOneField(Summary ,on_delete=models.CASCADE) 