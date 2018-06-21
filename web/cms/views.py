from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,reverse
from cms.forms import cms_loginForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
from frontauth.models import frontAuthModel,authReationModel
from article.models import ArticleModel,CommentModel
from django.conf import settings
from random import randint
from cms.utils import makeAuthors
from django.db.models import Count
# Create your views here.

#current_page指当前页，count指文章或者注册用户数量
def page(current_page,count):
	#当前页展示的用户或者文章数量
	c_authors = settings.C_AUTHORS
	#当前页
	c_page = int(current_page)
	#所有的注册用户，这是queryset
	all_pages = count/c_authors
	if count%c_authors != 0:
		#总页数
		all_pages = int(all_pages) + 1
	else:
		all_pages = int(all_pages)
	#切片开始和结束的位置
	end = c_page*c_authors
	begin = end - c_authors
	#显示的分页数[1,2,3,4,5]
	pages = []
	#向前找
	temp = c_page-1
	while temp>0:
		if temp%5 == 0:
			break
		else:
			pages.append(temp)
			temp -= 1
	#向后找
	temp = c_page
	while temp<=all_pages:
		if temp%5 == 0:
			pages.append(temp)
			break
		else:
			pages.append(temp)
			temp += 1
	#排序后的pages
	pages.sort()
	print(pages)
	number = end - c_authors
	context = {
		'c_page': c_page,
		'pages': pages,
		'all_pages': all_pages,
		'number': number
	}
	return (context,(begin,end))

@login_required
def cms_index(request,current_page=1):
	# sessionid = request.COOKIES.get('sessionid')
	# print('-'*10)
	# sqlsession = Session.objects.filter(session_key=sessionid).first()
	# print('sqlsession:',model_to_dict(sqlsession))
	# print('-'*10)
	# request.session['chenbin'] = 998
	# print('request.session:',request.session.items())
	# print('-'*10)
	# print('request.session.session_key:',request.session.session_key)
	# print('-'*10)
	# print(dir(request.session))
	#所有的注册用户，这是queryset
	authors = frontAuthModel.objects.all().order_by('-regist_time')
	authors_count = authors.count()
	page_result = page(current_page,authors_count)
	context0 = page_result[0]
	begin = page_result[1][0]
	end = page_result[1][1]
	authors_dice = authors[begin:end]
	context = {
		'authors': authors_dice,
	}
	context.update(context0)
	return render(request,'cms_index.html',context=context)

@require_http_methods(['GET','POST'])
def cms_login(request):
	if request.method == 'GET':
		return render(request,'cms_login.html')
	else:
		form = cms_loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			remember = form.cleaned_data.get('remember')
			next_url  = request.GET.get('next')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				if remember:
					request.session.set_expiry(None)
				else:
					request.session.set_expiry(0)
				if next_url:
					return redirect(next_url)
				else:
					return redirect(reverse('cms_index'))
			else:
				return HttpResponse('用户名或者密码错误！')
		else:
			return JsonResponse(form.errors)


def cms_article_manager(request,current_page=1):
	articles = ArticleModel.objects.annotate(num_comment=Count('commentmodel')).order_by('release_time')
	article_count = articles.count()
	page_result = page(current_page,article_count)
	begin = page_result[1][0]
	end = page_result[1][1]
	article_dice = articles[begin:end]
	context0 = page_result[0]
	context = {
		'articles':article_dice
	}
	context.update(context0)
	return render(request,'cms_article_manage.html',context)


@login_required
def cms_test(request):
	# author_list = makeAuthors(10)
	# for author in author_list:
	# 	print(author)
	# # auth = frontAuthModel(**kwargs)
	# # auth.save()
	# return HttpResponse('测试页面！')
	kwargs = {
		'title':'刮刮乐',
		'content_html':'400块给不给'
	}
	article = ArticleModel(**kwargs)
	article.save()
	return HttpResponse('这里是测试页面')