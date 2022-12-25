from django.db import models

# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=20000)
    create_date = models.DateTimeField()