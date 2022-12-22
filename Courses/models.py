from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=100)
    describtion = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bewertung = models.TextField(max_length=500)
    language = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='Courses_author', on_delete=models.CASCADE)
    video = models.FileField(upload_to='Courses/')
    img = models.ImageField(upload_to='Courses/')
    date = models.DateField()