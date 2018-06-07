from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from mytest.models import test_Model
from mytest.forms import testForm,testbForm
from django.core.cache import caches,cache
# Create your views here.

def mytest_index(request):
	cache.set('my_key', 'hello, world!', 30)
	print('cache value:',cache.get('my_key'))
	print('caches:',caches.all())
	form = testbForm()
	return render(request,'test.html',context={'form':form})
