from django.utils.deprecation import MiddlewareMixin
from frontauth.configs import LOGIN_KEY
from frontauth.models import frontAuthModel
#给request设置frontuser的中间件
class frontAuthenticationMiddleware(MiddlewareMixin):
	def process_request(self,request):
		# print('-'*30)
		# print(request.session)
		# print('-'*30)
		uid = request.session.get(LOGIN_KEY,None)
		print('-'*30)
		print(uid)
		print('-'*30)
		if uid:
			if hasattr(request,'frontuser'):
				return
			else:
				frontuser = frontAuthModel.objects.filter(pk=uid).first()
				request.frontuser = frontuser






			

