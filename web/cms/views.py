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
from django.conf import settings
# Create your views here.

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
	c_authors = settings.C_AUTHORS
	#当前页
	c_page = int(current_page)
	#所有的注册用户，这是queryset
	authors = frontAuthModel.objects.all().order_by('-regist_time')
	authors_count = authors.count()
	all_pages = authors_count/c_authors
	if authors_count%c_authors != 0:
		#总页数
		all_pages = int(all_pages) + 1
	else:
		all_pages = int(all_pages)
	#切片开始和结束的位置
	end = c_page*c_authors
	begin = end - c_authors
	#每页的文章切片
	authors_dice = authors[begin:end]
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
	context = {
		'authors':authors,
		'c_page':c_page,
		'authors':authors_dice,
		'pages':pages,
		'all_pages':all_pages
	}
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

@login_required
def cms_test(request):
	kwargs = {'username':'汪峰','tel':'1865451234','email':'wangfeng@sina.com','password':'123456'}
	# auth = frontAuthModel(username='陈斌',tel='1383838438',email='151251@qq.com',password='123456')
	auth = frontAuthModel(**kwargs)
	auth.save()
	return HttpResponse('测试页面！')