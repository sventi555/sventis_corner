from django.contrib import admin
from . import models


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


@admin.register(models.TaliaText)
class TaliaTextAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'date',
    )
