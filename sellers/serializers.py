from rest_framework import serializers  
from .models import Sellers, Charge 
from django.contrib.auth.models import User 


class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'password', 'email']  # Include necessary fields  

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  # Hash the password  
        user.save()  
        return user  

class SellersSerializer(serializers.ModelSerializer):  
    user = UserSerializer()  # Include the user serializer  

    class Meta:  
        model = Sellers  
        fields = ['id', 'name', 'user', 'registration_date', 'inventory', 'is_active']   

    def create(self, validated_data):  
        user_data = validated_data.pop('user')  # Get user data  
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)  
        client = Sellers.objects.create(user=user, **validated_data)  # Create client with user  
        return client
    


class ChargeSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Charge  
        fields = ['id', 'amount', 'request_time', 'confirmed_by', 'confirmed_time', 'is_confirmed']