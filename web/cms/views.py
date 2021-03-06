from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,reverse
from cms.forms import cms_loginForm,cmsfrontAuthForm,cmsArticleQueryForm,cmsAddCategoryForm,cmsAddTagForm,cmsTopArticleForm,cmsDeleteArticleForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
from frontauth.models import frontAuthModel,authReationModel
from article.models import ArticleModel,CommentModel,CategoryModel,SupportModel,TagModel,TopModel
from django.conf import settings
from random import randint
from cms.utils import makeAuthors
from django.db.models import Count
from cms.forms import cmsDeleteAuthorForm,cmsArticleModifyForm
from utils import bnjson
from django.utils import timezone
from django.db.models import Q,F
from django.db import connection

from frontauth.hashers import make_password
from frontauth import front_login,front_logout
from frontauth.configs import LOGIN_KEY
from frontauth.decorators import front_login_required

# Create your views here.

#current_page指当前页，query_result指queryset的查询结果,query_name指的是切片的key名称
def page(current_page,query_result,query_name):
	#count指文章或者注册用户数量
	count = len(query_result)
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
	query_dice = query_result[begin:end]
	if bool(query_dice) == False:
		c_page = 1
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
	number = end - c_authors
	context = {
		'c_page': c_page,
		'pages': pages,
		'all_pages': all_pages,
		'number': number,
		 query_name: query_dice
	}
	return context

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
	c_page = int(current_page)
	authors = frontAuthModel.objects.all().order_by('-regist_time')
	context = page(c_page,authors,query_name='authors')
	return render(request,'cms_index.html',context=context)

@require_http_methods(['POST'])
def cms_author_delete(request):
	form = cmsDeleteAuthorForm(request.POST)
	if form.is_valid():
		uid = form.cleaned_data.get('author_uid')
		author = frontAuthModel.objects.filter(pk=uid).first()
		if author:
			author.delete()
			return bnjson.json_result(message='该用户已被删除')
		else:
			return bnjson.json_params_error(message='没有该用户！')
	else:
		return form.error_json_resopnse()

# @login_required
@require_http_methods(['POST','GET'])
def cms_author_modify(request,uid):
	if request.method == 'GET':
		author = frontAuthModel.objects.filter(pk=uid).first()
		context={
			'author':author
		}
		return render(request,'cms_author_modify.html',context=context)
	else:
		form = cmsfrontAuthForm(request.POST)
		if form.is_valid():
			# print('-'*30)
			# print(type(form.cleaned_data))
			# print('-'*30)
			author = frontAuthModel.objects.filter(pk=uid).first()
			new_psw = form.cleaned_data.get('new_psw')
			author.password = new_psw
			author.save(update_fields=['password'])
			context={
			'author':author,
			'modify_result':'密码修改成功！'
			}
			return render(request,'cms_author_modify.html',context=context)
		else:
			error_dict = form.errors.as_data()
			# print(error_dict)
			message = ''
			for key in error_dict.keys():
				message = error_dict[key][0]
				break
			#将ValidationError中的字符串提取出来
			message = message.messages[0]
			author = frontAuthModel.objects.filter(pk=uid).first()
			context={
			'author':author,
			'modify_fail':message
			}
			# print(form.errors.as_data()['new_psw'][0].messages[0])
			return render(request,'cms_author_modify.html',context=context)

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

def cms_logout(request):
	logout(request)
	return redirect('cms_login')

@login_required
@require_http_methods(['GET'])
def cms_article_manager(request):
	return render(request,'cms_article_manage.html')

@login_required
@require_http_methods(['POST'])
def cms_article_query(request):
	form = cmsArticleQueryForm(request.POST)
	if form.is_valid():
		title = form.cleaned_data.get('title')
		author = form.cleaned_data.get('author')
		category = form.cleaned_data.get('category')
		c_page = form.cleaned_data.get('c_page')
		#目前只能按标题查询，此处有待完善
		articles = ArticleModel.objects.filter(Q(title__contains=title)&Q(author__username__contains=author)&Q(category__name__contains=category))
		article_list = list(articles.annotate(author_name=F('author__username'),category_name=F('category__name')).values('uid','title','author_name','category_name','release_time','read_count','top').order_by('-top__top_time','-release_time'))
		for article in article_list:
			if article['top']:
				article['top']=True
			else:
				article['top']=False
		context = page(c_page,article_list,query_name='article')
		return bnjson.json_result(message='查询成功！',data=context)
	else:
		return form.error_json_resopnse()

# @login_required
@require_http_methods(['GET','POST'])
def cms_article_modify(request,uid):
	if request.method == 'GET':
		article = ArticleModel.objects.filter(pk=uid).first()
		categorys = CategoryModel.objects.all().order_by('pk')
		tags = TagModel.objects.all().order_by('pk')
		if article:
			context = {
				'article': article,
				'categorys': categorys,
				'tags': tags,
				'article_tags': list(article.tags.values_list('id',flat=True))
			}

			return render(request,'cms_article_modify.html',context=context)
		else:
			return bnjson.json_params_error(message='没有这篇文章')

	else:
		form = cmsArticleModifyForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			category_id = form.cleaned_data.get('category_id')
			category = CategoryModel.objects.filter(id=category_id).first()
			content = form.cleaned_data.get('content')
			article = ArticleModel.objects.filter(pk=uid).first()
			article.title = title
			article.category = category
			article.content_html = content
			article.save(update_fields=['title','category','content_html','update_time'])
			tagIds = request.POST.getlist('tagIds')
			tags = []
			if tagIds:
				for tag_id in tagIds:
					tag = TagModel.objects.filter(pk=tag_id).first()
					if tag:
						tags.append(tag)
				print(tags)
				article.tags.set(tags)
			return bnjson.json_result(message='修改成功')
		else:
			return form.error_json_resopnse()

@login_required
@require_http_methods(['POST'])
def cms_article_delete(request):
	form = cmsDeleteArticleForm(request.POST)
	if form.is_valid():
		uid = form.cleaned_data.get('uid')
		article = ArticleModel.objects.filter(pk=uid).first()
		if article:
			data = model_to_dict(article,fields=['title','author__username'])
			article.delete()
			return bnjson.json_result(message='文章已删除',data=data)
		else:
			return bnjson.json_params_error(message='没有这篇文章，无法删除')
	else:
		return form.error_json_resopnse()

# @login_required
@require_http_methods(['POST'])
def cms_article_top(request):
	form = cmsTopArticleForm(request.POST)
	if form.is_valid():
		uid = form.cleaned_data.get('uid')
		article = ArticleModel.objects.filter(pk=uid).first()
		if article:
			if article.top:
				article.top.save()
				# article.save(update_fields=['top'])
				return bnjson.json_result(message='已再次置顶')
			else:
				top = TopModel()
				top.save()
				article.top = top
				article.save(update_fields=['top'])
				return bnjson.json_result(message='已置顶')
		else:
			return bnjson.json_params_error(message='没有这篇文章，无法置顶')
	else:
		return form.error_json_resopnse()

@require_http_methods(['POST'])
def cms_article_untop(request):
	form = cmsTopArticleForm(request.POST)
	if form.is_valid():
		uid = form.cleaned_data.get('uid')
		article = ArticleModel.objects.filter(pk=uid).first()
		if article:
			if article.top:
				article.top.delete()
				return bnjson.json_result(message='已取消置顶')
			else:
				bnjson.json_params_error(message='这篇文章未置顶，无法进行置顶操作')
		else:
			return bnjson.json_params_error(message='没有这篇文章，无法置顶')
	else:
		return form.error_json_resopnse()


@login_required
@require_http_methods(['POST'])
def cms_add_category(request):
	form = cmsAddCategoryForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data.get('name')
		category = CategoryModel.objects.filter(name=name).first()
		if category:
			return bnjson.json_params_error(message='该分类已存在')
		else:
			category = CategoryModel(name=name)
			category.save()
			data = {
				'id': category.id,
				'name': category.name
			}
			return bnjson.json_result(data=data)
	else:
		return form.error_json_resopnse()

# @login_required
@require_http_methods(['POST'])
def cms_add_tag(request):
	form = cmsAddTagForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data.get('name')
		tag = TagModel.objects.filter(name=name).first()
		if tag:
			return bnjson.json_params_error(message='该标签已存在')
		else:
			tag = TagModel(name=name)
			tag.save()
			data = {
				'id': tag.id,
				'name': tag.name
			}
			return bnjson.json_result(data=data)
	else:
		return form.error_json_resopnse()

# @login_required
@front_login_required
def cms_test(request):
	# kwargs = {
	# 	'username': '皮诺曹',
	# 	'tel': '15885854683',
	# 	'email': '999888@qq.com',
	# 	'password': '123456'
	# }
	# user = frontAuthModel.objects.filter(tel='15885854683').first()
	# temp = front_login(request,user,'1234567')
	# front_logout(request)
	return render(request,'test.html')