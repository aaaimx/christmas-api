from .models import *
from rest_framework import serializers

class VillaSerializer(serializers.ModelSerializer):
  class Meta:
    model = villa
    fields = '__all__'

class ModulesSerializer(serializers.ModelSerializer):
  class Meta:
    model = modules
    fields = '__all__'
  