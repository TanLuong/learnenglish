from django.contrib import admin
from .models import Ieltsstories
# Register your models here.
@admin.register(Ieltsstories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
