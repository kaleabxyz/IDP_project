from rest_framework import serializers
from .models import *

class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
class PatientSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Patient
        fields = '__all__'
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'roomnumber', 'availability']
        
        