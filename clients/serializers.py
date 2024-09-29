from rest_framework import serializers
from sellers.models import Sellers
from .models import Client, ChargeRequests
from utils.validators import phone_number_validator

class ClientSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Client  
        fields = ['id', 'phone_number', 'registration_date', 'inventory', 'is_active']



class ClientChargeSerializer(serializers.ModelSerializer):
    class Meta:  
        model = ChargeRequests  
        fields = '__all__'



class ChargeRequestSerializer(serializers.ModelSerializer):  
    phone_number = serializers.CharField(max_length=13, validators=[phone_number_validator])
    amount = serializers.IntegerField()

    class Meta:
        model = ChargeRequests
        fields = ['phone_number', 'amount']

    def validate(self, attrs):
        if attrs['amount'] <= 0:
            raise serializers.ValidationError("Amount must be a positive integer.")
        return attrs
