from rest_framework import serializers


from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

from equation.models import Equation, Example
class ExampleSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Example
        fields = '__all__'

class EquationSerializer(serializers.ModelSerializer):
    examples= ExampleSerializer(many=True)
    class Meta:
        model = Equation
        fields = '__all__'
        read_only_fields = ['id', 'createt_at', 'updated_at']





