from rest_framework import serializers
from .models import Appointments
from django_jalali.serializers.serializerfield import JDateField

class AppointmentSerializer(serializers.ModelSerializer):
    date = JDateField()
    class Meta:
        model = Appointments
        fields = ['first_name','last_name','phone','email','date','time']

class UserSerializer(serializers.ModelSerializer):
    date = JDateField()
    class Meta:
        model = Appointments
        fields = ['first_name','last_name','phone','email','date','time']
    def create(self, validated_data):
        user = Appointments (first_name=validated_data['first_name'],last_name=validated_data['last_name'],phone=validated_data['phone'],email=validated_data['email'],date=validated_data['date'],time=validated_data['time'])
        user.save()
        return user



