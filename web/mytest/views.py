from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from mytest.models import test_Model
# Create your views here.

def mytest_index(request):
	test = test_Model(username='sudo',password='123456')
	test.save()
	return HttpResponse('test success！')
