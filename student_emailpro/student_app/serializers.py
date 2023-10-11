from rest_framework import serializers
from .models import StudentM

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentM
        fields='__all__'