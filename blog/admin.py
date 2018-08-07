from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
    ]

    list_display = (
        'id',
        'title',
        'date',
    )
