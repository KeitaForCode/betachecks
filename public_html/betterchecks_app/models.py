from django.db import models
from django_countries.fields import CountryField


# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=256)
    message = models.CharField(max_length=2000)
    file = models.FileField(upload_to='user_files',blank=True)
    
    def __str__(self):
        return self.name
    
class CourseEnquiry(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField()
    country = CountryField()
    organization = models.CharField(max_length=500)
    interest = models.CharField(max_length=500)
        
    def __str__(self):
        return self.name
     
    
class Contacts(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=256)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name