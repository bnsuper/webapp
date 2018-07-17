
from frontauth.configs import LOGIN_KEY
#前台用户登录功能
def front_login(request,user,raw_password):
	#如果密码正确
	if user.check_password(raw_password):
		request.session[LOGIN_KEY] = str(user.pk)
		# print(request.session[LOGIN_KEY])
		return user
	else:
		return None


def front_logout(request):
	if LOGIN_KEY in request.session.keys():
		request.session.pop(LOGIN_KEY)
	# print(request.session.get(LOGIN_KEY,'front session has been deleted. It is nothing'))