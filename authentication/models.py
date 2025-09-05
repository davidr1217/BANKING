from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    
class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    
