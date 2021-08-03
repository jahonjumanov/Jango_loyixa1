from django.db import models

# Create your models here.
class Meva(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.CharField(max_length=2048)
    desc = models.CharField(max_length=255)
    price = models.FloatField()