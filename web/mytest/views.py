from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from mytest.models import test_Model
from mytest.forms import testForm,testbForm
from django.core.cache import caches,cache
from django.db.models import F
from django.db import connection
from django.db.models.expressions import RawSQL
from article.models import ArticleModel,CategoryModel,TagModel
from django.db.models.query import RawQuerySet
# Create your views here.

def mytest_index(request):
	# cache.set('my_key', 'hello, world!', 30)
	# print('cache value:',cache.get('my_key'))
	# print('caches:',caches.all())
	# form = testbForm()
	# return render(request,'test.html',context={'form':form})

	# testmodel = test_Model.objects.filter(pk=1).first()
	# testmodel.number = F('number') + 1
	# testmodel.save()
	# print('-'*30)
	# print(connection.queries)
	# print('-'*30)

	articles = ArticleModel.objects.raw('SELECT * FROM article_articlemodel')
	print(type(articles))
	for s in articles:
		print(type(s))
		print(s.title)

	return HttpResponse('ok')

