from .models import *
from rest_framework import serializers

class VillaSerializer(serializers.ModelSerializer):
  class Meta:
    model = villa
    fields = '__all__'

class VillaSerializer(serializers.ModelSerializer):
  class Meta:
    model = villa
    fields = '__all__'
  