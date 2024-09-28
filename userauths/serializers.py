from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
    
    
class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = '__all__'
