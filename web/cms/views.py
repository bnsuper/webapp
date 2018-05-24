from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.

def cms_index(request):
	return HttpResponse('这里是后台管理系统首页！')