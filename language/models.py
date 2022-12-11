from django.db import models


class Transalation(models.Model):
    text = models.JSONField(null=True, blank=True)
