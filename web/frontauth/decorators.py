
from frontauth import configs
from django.shortcuts import redirect
#登录装饰器
def front_login_required(func,login_url=None):
	if login_url is None:
		login_url = configs.LOGIN_URL
	def wrapper(request,*args,**kwargs):
		if request.session.get(configs.LOGIN_KEY):
			return func(request,*args,**kwargs)
		else:
			url = login_url + '?next=' + request.path
			return redirect(url)
	return wrapper