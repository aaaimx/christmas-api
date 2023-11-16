from django.db import models
import uuid

# Create your models here.
class modules(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  address = models.CharField(max_length=10, null=False, blank=False)
  created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
  updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.id
  
class villa(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
  updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.id
