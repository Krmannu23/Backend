from django.db import models

#https://docs.djangoproject.com/en/5.0/topics/db/models/
#jaha foreign key use hua wuska sinle father hoga ,child ka details bharne ke liye father table ka details ho chahiye
class Subject(models.Model):
    subject = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
    ]
    subject_id=models.UUIDField(primary_key=True)
    subject_name=models.CharField(choices=subject,max_length=30)
    points_or_marks=models.FloatField()

class Name(models.Model):#https://docs.djangoproject.com/en/5.0/ref/models/fields/
    titles_options =[
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
    ]
    titles=models.CharField(max_length=30 ,choices=titles_options)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

class Address(models.Model):
    address_id=models.UUIDField(primary_key=True)
    adress_line_1=models.CharField(max_length=30)
    address_line2=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

class OtherDetails(models.Model):
    id_number=models.CharField(max_length=30,primary_key=True)
    contact_number=models.PositiveIntegerField()
    email_id=models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    

class Tenth(models.Model):
    ten_id=models.UUIDField(primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insert_date=models.DateTimeField()


class Twelfth(models.Model):
    Twelfth_id=models.UUIDField(primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insert_date=models.DateTimeField()
class College(models.Model):
    College_id=models.UUIDField(primary_key=True)
    sem = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
    ]
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    insert_date=models.DateTimeField()
    seamster=models.CharField(max_length=30,choices=sem)

class ParentDetails(models.Model):
    parent_id=models.UUIDField(primary_key=True)
    parent_name=models.OneToOneField(Name, on_delete=models.CASCADE)
    other_details=models.OneToOneField(OtherDetails, on_delete=models.CASCADE)
    relationship=models.CharField(max_length=30)
class BasicDetails(models.Model):
    user_id=models.UUIDField(primary_key=True)
    name=models.OneToOneField(Name, on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    other_details=models.OneToOneField(OtherDetails, on_delete=models.CASCADE)
    parentInfo=models.OneToOneField(ParentDetails, on_delete=models.CASCADE)
class TenSchoolingDetails(models.Model):
    tenth_roll_no=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Matriculation roll number cannot be empty'})
    school_name=models.CharField(max_length=30)
    board_name=models.CharField(max_length=30)
    date_of_enrollment=models.CharField(max_length=30)
    year_of_passing=models.CharField()
    insert_date=models.DateTimeField()
    year_of_passing=models.CharField(max_length=30)


class TwelfthSchoolingDetails(models.Model):
    school_name=models.CharField(max_length=30)
    board_name=models.CharField(max_length=30)
    date_of_enrollment=models.CharField(max_length=30)
    year_of_passing=models.CharField()
    twelfth_roll_no=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'Inter roll number cannot be empty'})
    insert_date=models.DateTimeField()
    year_of_passing=models.CharField(max_length=30)
class CollegeDetails(models.Model):
    college_name=models.CharField(max_length=30)
    university_name=models.CharField(max_length=30)
    date_of_enrollment=models.CharField(max_length=30)
    college_roll_no=models.PositiveIntegerField(blank=False ,primary_key=True,error_messages={'message':'College roll number cannot be empty'})
    insert_date=models.DateTimeField()
    year_of_passing=models.CharField(max_length=30)


class Resume(models.Model):
    resume_id=models.UUIDField(primary_key=True)
    title=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    contact_number=models.PositiveIntegerField()
    
class FullApi(models.Model):
    basic_details = models.OneToOneField(BasicDetails, on_delete=models.CASCADE)
    tenth_schooling_details = models.OneToOneField(TenSchoolingDetails, on_delete=models.CASCADE)
    twelfth_schooling_details = models.OneToOneField(TwelfthSchoolingDetails, on_delete=models.CASCADE)
    college_details = models.OneToOneField(CollegeDetails, on_delete=models.CASCADE)
    tenth = models.OneToOneField(Tenth, on_delete=models.CASCADE)
    twelfth = models.OneToOneField(Twelfth, on_delete=models.CASCADE)
    college = models.OneToOneField(College, on_delete=models.CASCADE)