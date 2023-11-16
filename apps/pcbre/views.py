from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .services import *
from rest_framework.decorators import action

# Create your views here.
class VillaViewSet(viewsets.ModelViewSet):
  queryset = villa.objects.all()
  serializer_class = VillaSerializer
  permission_classes = [permissions.AllowAny]

  @action(detail=False, methods=['GET'])
  def gpio(self, request, *args, **kargs):
    on_led()

class ModulesViewSet(viewsets.ModelViewSet):
  queryset = modules.objects.all()
  serializer_class = ModulesSerializer
  permission_classes = [permissions.AllowAny]