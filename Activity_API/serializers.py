from rest_framework import serializers
from .models import MyTask

class MyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTask
        fields = '__all__'