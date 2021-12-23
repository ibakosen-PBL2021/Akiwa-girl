from django.db import models

# Create your models here.
class Occupancy(models.Model):
    id = models.IntegerField(primary_key=True)
    occupancy = models.BooleanField(default=False)
