from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,reverse
from cms.forms import cms_loginForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict

# Create your views here.

@login_required
def cms_index(request):
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
	return render(request,'cms_index.html')

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
	return HttpResponse('测试页面！')