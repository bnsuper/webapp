from django.contrib import admin
from mytest.models import test_Model

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	pass

admin.site.register(test_Model,AuthorAdmin)