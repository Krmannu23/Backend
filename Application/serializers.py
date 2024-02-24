from rest_framework import serializers
from . import models

class TenthSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tenth
        fields='__all__'

class TwelfthSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Twelfth
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.College
        fields='__all__'


class BasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BasicDetails
        fields='__all__'

class SchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SchoolingDetails
        fields='__all__'

class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CollegeDetails
        fields='__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Resume
        fields='__all__'