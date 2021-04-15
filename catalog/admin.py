from django.contrib import admin
from .models import ieltsstories, ieltstest

# Register your models here.
@admin.register(ieltsstories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

@admin.register(ieltstest)
class TestAdmin(admin.ModelAdmin):
    list_display = ['qnumber', 'qcontent']
