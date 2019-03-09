from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class TaliaText(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-id']
