from django.db import models


class Graphic(models.Model):
    title = models.CharField(max_length=140, unique=True)
    link = models.TextField()
    description = models.TextField()

