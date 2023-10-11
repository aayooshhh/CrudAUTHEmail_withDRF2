from rest_framework import serializers
from django.contrib.auth import get_user_model


user=get_user_model()


class userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=user
        fields=('id','username','password','email','first_name','last_name')
    def create(self, validated_data):
        return user.objects.create_user(**validated_data)