from django.contrib import admin
from mytest.models import test_Model,testb_Model

# Register your models here.
def make_published(modeladmin,request,queryset):
	queryset.update(status='p')
make_published.short_description = 'Mark selected stories as published'

class AuthorAdmin(admin.ModelAdmin):
	list_display=['username','email','status']
	ordering = ['username']
	actions = [make_published]

admin.site.register(test_Model,AuthorAdmin)

admin.site.register(testb_Model)