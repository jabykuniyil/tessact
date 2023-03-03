from rest_framework import serializers
from .models import UserProfile


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_name',
            'email_id',
            'first_name',
            'last_name',
            'password',
            'dob',
            'phone_number',
            'address',
            'notify_user'
        ]
