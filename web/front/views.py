from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from article.models import ArticleModel,CategoryModel
from front.utils import page
from utils import bnjson
from django.views.decorators.http import require_http_methods
from front.forms import FrontPageForm
from django.db.models import Count
from django.db.models import F
from django.db import connection
from django.forms.models import model_to_dict

# Create your views here.
@require_http_methods(['GET'])
def front_index(request):
	if request.is_ajax():
		form = FrontPageForm(request.GET)
		if form.is_valid():
			c_page = form.cleaned_data.get('c_page')
			untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time')
			data = page(c_page,untop_articles,'untop_articles')
			temp = []
			slice_articles = data['untop_articles']
			for untop_article in slice_articles:
				count = untop_article.commentmodel_set.count()
				if count:
					count_dic = untop_article.commentmodel_set.aggregate(count=Count(F('commentreplymodel')))
					comment_count = count_dic['count']
				else:
					comment_count = 0
				support_count = untop_article.supports.filter(status=1).count()
				article = {}
				article['content_html'] = untop_article.content_html
				article['title'] = untop_article.title
				article['author__username'] = untop_article.author.username
				article['comment_count'] = comment_count
				article['support_count'] = support_count
				article['uid'] = untop_article.uid
				temp.append(article) 
			data['untop_articles'] = temp
			return bnjson.json_result(message='数据获取成功',data=data)
		else:
			return form.error_json_resopnse()
	else:
		# 查找被置顶的文章,最多只能置顶3篇文章
		articles = ArticleModel.objects.filter(top__isnull=False,supports__status=1).annotate(support_times=Count('supports'))
		print(articles.query)
		print('-'*30)

		top_articles = ArticleModel.objects.filter(top__isnull=False).order_by('-top__top_time')
		for top_article in top_articles:
			support_count = top_article.supports.filter(status=1).count()
			top_article.support_count = support_count
		# print(top_articles.query)
		# print('++++++++++++++++++++++++')
		untop_articles = ArticleModel.objects.filter(top__isnull=True).order_by('-release_time')
		for untop_article in untop_articles:
			support_count = untop_article.supports.filter(status=1).count()
			untop_article.support_count = support_count
		#查询文章分类信息
		categorys = CategoryModel.objects.annotate(count=Count(F('articlemodel'))).order_by('-count').values()
		categorys = categorys[0:7]
		context = page(1,untop_articles,'untop_articles')
		for untop_article in context['untop_articles']:
			count = untop_article.commentmodel_set.count()
			if count:
				count_dic = untop_article.commentmodel_set.aggregate(count=Count(F('commentreplymodel')))
				untop_article.comment_count = count_dic['count']
			else:
				untop_article.comment_count = 0
		for top_article in top_articles:
			count = top_article.commentmodel_set.count()
			if count:
				count_dic = top_article.commentmodel_set.aggregate(count=Count(F('commentreplymodel')))
				top_article.comment_count = count_dic['count']
			else:
				top_article.comment_count = 0
		context['top_articles'] = top_articles
		context['categorys'] = categorys
		# print('测试')
		# print(context['top_articles'])
		# for x in context['top_articles']:
		# 	print('点赞数：',x.support_count)
		# print('测试')
		return render(request,'front_article_index.html',context=context)


def front_article(request,uid):
	article=ArticleModel.objects.filter(pk=uid).first()
	context= {
		'article':article
	}
	return render(request,'front_article_detail.html',context=context)