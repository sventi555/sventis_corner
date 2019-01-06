from django.db import models


class Graphic(models.Model):
    title = models.CharField(max_length=140, unique=True)
    iframe = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title

    class Meta:
        ordering = ['-date']


