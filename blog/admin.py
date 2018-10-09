from django.contrib import admin
from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
    ]

    inlines = [
        CommentInline,
    ]

    list_display = (
        'id',
        'title',
        'date',
    )
