from django.db import models

# Create your models here.
class Destinations(models.Model):
   
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()
    desc = models.TextField()
    offer = models.BooleanField(default=False)