from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from article.models import ArticleModel,CategoryModel,CommentModel,CommentReplyModel
from front.utils import page
from utils import bnjson
from django.views.decorators.http import require_http_methods
from front.forms import FrontPageForm
from django.db.models import Count
from django.db.models import F
from django.db import connection
from django.forms.models import model_to_dict
import re

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
	article.read_count = F('read_count') + 1
	article.save(update_fields=['read_count'])
	article.refresh_from_db()
	html = article.content_html
	dr = re.compile(r'(<[^>]+>)|(&nbsp;)|( )',re.S)
	dd = dr.sub('',html)
	print('-'*30)
	print(dd)
	print('-'*30)
	#添加文字数属性
	article.word_count = len(dd)
	#计算评论数
	main_comments = article.commentmodel_set
	main_comments_count = main_comments.count()
	sub_comments_count = main_comments.aggregate(count=Count('pk'))['count']
	#添加文章评论数量属性
	article.comment_count = main_comments_count + sub_comments_count
	#计算文章喜欢量
	article.support_count = article.supports.count()
	#作者
	author = article.author
	#该作者写的文章总字数
	word_count = 0
	articles  = author.articlemodel_set.all()
	for temp in articles:
		html = temp.content_html
		dd = dr.sub('',html)
		word_count += len(dd)
	#给作者添加word_count属性
	author.word_count = word_count
	#该作者被多少人关注
	attention_count = author.authBs.count()
	#给作者添加关注量属性
	author.attention_count = attention_count
	#该作者获得了多少喜欢
	like_count = articles.filter(supports__status=1).aggregate(count=Count('supports'))['count']
	#添加喜欢量属性
	author.like_count = like_count
	context= {
		'article':article,
		'author':author
	}
	return render(request,'front_article_detail.html',context=context)