from django.db import models


class Graphic(models.Model):
    title = models.CharField(max_length=140, unique=True)
    iframe = models.TextField()
    description = models.TextField()

    def __str__(self):
            return self.title


