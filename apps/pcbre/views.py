from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class VillaViewSet():
  queryset = villa.objects.all()
  serializer_class = VillaSerializer
  permission_classes = [permissions.AllowAny]

class ModulesViewSet():
  queryset = modules.objects.all()
  serializer_class = ModulesSerializer
  permission_classes = [permissions.AllowAny]