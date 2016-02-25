from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)
    reg_number = models.IntegerField(unique=True)
    age = models.IntegerField(default=25)
    address = models.TextField(max_length=1024)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
       
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

from django.contrib.auth.models import User
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

