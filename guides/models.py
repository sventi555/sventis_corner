from django.db import models

class Guide(models.Model):
    title = models.CharField(max_length=250)
    overview = models.TextField()
    requirements = models.TextField()
    process = models.TextField()
    wrapup = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
