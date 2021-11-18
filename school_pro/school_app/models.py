from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    school_website = models.URLField(max_length=264,blank=True,unique=False)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        return self.user.username


class School(models.Model):
    name = models.CharField(max_length=264)
    location = models.CharField(max_length=264)
    principle = models.CharField(max_length=264)
    main_branch = models.CharField(max_length=264)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=264)
    tenth = models.PositiveIntegerField()
    ninth = models.PositiveIntegerField()
    eighth = models.PositiveIntegerField()
    seventh = models.PositiveIntegerField()
    sixth = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:thank')
