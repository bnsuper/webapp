from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from mytest.models import test_Model
from mytest.forms import testForm,testbForm
# Create your views here.

def mytest_index(request):
	form = testbForm()
	return render(request,'test.html',context={'form':form})
