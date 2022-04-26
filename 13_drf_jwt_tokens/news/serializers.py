from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()

class UserValidateSerializer(serializers.Serializer):

    def decode_and_authorize(self, validated_data):
        email = "dk@gmail.com"
        
        user = User.objects.filter(email=email).first()

        if user:
            return user
        else:
            raise serializers.ValidationError({'msg': 'error'})