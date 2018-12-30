from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Categories'


class Guide(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

