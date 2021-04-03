from django.contrib import admin
from .models import ieltsstories
# Register your models here.
@admin.register(ieltsstories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
