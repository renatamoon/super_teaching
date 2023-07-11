# STANDARD IMPORTS
from rest_framework import serializers

# PROJECT IMPORTS
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
