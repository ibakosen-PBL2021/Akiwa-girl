from django.db import models

# Create your models here.
class Current(models.Model):
    num = models.IntegerField(default=0)
