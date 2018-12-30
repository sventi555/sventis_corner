from django.contrib import admin
from guides import models

admin.site.register(models.Guide)
admin.site.register(models.Category)

# @admin.register(models.Guide)
# class GuideAdmin(admin.ModelAdmin):
    
