from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from article.models import ArticleModel,CategoryModel
from front.utils import page
from utils import bnjson
from django.views.decorators.http import require_http_methods
from front.forms import FrontPageForm
from django.db.models import Count

# Create your views here.
@require_http_methods(['GET'])
def front_index(request):
	if request.is_ajax():
		form = FrontPageForm(request.GET)
		if form.is_valid():
			c_page = form.cleaned_data.get('c_page')
			untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time').values('author__username','title','content_html')
			data = page(c_page,untop_articles,'untop_articles')
			data['untop_articles'] = list(data['untop_articles'])
			return bnjson.json_result(message='数据获取成功',data=data)
		else:
			return form.error_json_resopnse()
	else:
		# 查找被置顶的文章,最多只能置顶3篇文章
		top_articles = ArticleModel.objects.filter(top__isnull=False).order_by('-top__top_time')
		#查找未被置顶的文章
		untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time')
		#查询文章分类信息
		categorys = CategoryModel.objects.annotate(count=Count('articlemodel')).order_by('-count').values()
		categorys = categorys[0:7]
		context = page(1,untop_articles,'untop_articles')
		print(top_articles)
		context['top_articles'] = top_articles
		context['categorys'] = list(categorys)
		return render(request,'front_article_index.html',context=context)

		


# @require_http_methods(['GET'])
# def front_index(request):
# 	if request.method == 'GET':
# 		# 查找被置顶的文章,最多只能置顶3篇文章
# 		top_articles = ArticleModel.objects.filter(top__isnull=False).order_by('-top__top_time')
# 		#查找未被置顶的文章
# 		untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time')
# 		#查询文章分类信息
# 		categorys = CategoryModel.objects.annotate(count=Count('articlemodel')).order_by('-count').values()
# 		categorys = categorys[0:7]
# 		context = page(1,untop_articles,'untop_articles')
# 		print(top_articles)
# 		context['top_articles'] = top_articles
# 		context['categorys'] = list(categorys)
# 		return render(request,'front_article_index.html',context=context)
# 	else:
# 		if request.is_ajax():
# 			form = FrontPageForm(request.POST)
# 			if form.is_valid():
# 				c_page = form.cleaned_data.get('c_page')
# 				untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time').values()
# 				data = page(c_page,untop_articles,'untop_articles')
# 				data['untop_articles'] = list(data['untop_articles'])
# 				return bnjson.json_result(message='数据获取成功',data=data)
# 			else:
# 				return form.error_json_resopnse()
# 		else:
# 			return bnjson.json_params_error(message='不受理该请求')