from django.db import models


class Url(models.Model):
    urlLarga = models.CharField(max_length=128)
