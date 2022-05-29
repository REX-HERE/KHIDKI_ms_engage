from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES=(
    ('All', 'All'),
    ('Kids','Kids')
)

MOVIE_TYPE=(
    ('single','single'),
    ('seasonal','seasonal')
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    movie_id = models.IntegerField(default= -12, unique=True)
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE,default='single')
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES, default='All',blank=True,null=True)

    # class Meta:
    #     db_table = "web_member"


class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')


class Dropdown(models.Model):
    title:str=models.CharField(max_length=225, default='title_d')

    def __str__(self):
        return self.title








