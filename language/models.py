from django.db import models

# Create your models here.
class Transalation(models.Model):
    text = models.JSONField(null=True, blank=True)