from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class People_Comments(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=40)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    image = models.ImageField(upload_to='people_pics')
