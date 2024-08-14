from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation


    
class About(models.Model):
    image = models.ImageField(upload_to='Images/about')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"


class Service(models.Model):
    image = models.ImageField(upload_to='Images/service')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
 
class Team(models.Model):
    image = models.ImageField(upload_to='Images/team')
 

    
 
class Client(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/client')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title