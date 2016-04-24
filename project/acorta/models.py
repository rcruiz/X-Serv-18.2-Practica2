from django.db import models

# Create your models here.


class Url(models.Model):
    urlLarga = models.CharField(max_length=120)
    urlCorta = models.IntegerField()
