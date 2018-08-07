from django.contrib import admin
from . import models


# Register your models here.

def delete_selected_instances(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()


admin.site.register(models.FileType)


class FileInline(admin.StackedInline):
    model = models.File


class ThumbnailInline(admin.StackedInline):
    model = models.Thumbnail


@admin.register(models.Graphic)
class GraphicAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'description',
    ]

    list_display = [
        'id',
        'title',
        'date',
    ]

    inlines = [ThumbnailInline, FileInline]

    actions = [delete_selected_instances]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
