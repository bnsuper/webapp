from django.db import models
import uuid
from frontauth.hashers import make_password
# Create your models here.

#注册用户模型
class frontAuthModel(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	username = models.CharField(max_length=20,unique=True)
	tel = models.CharField(max_length=20,unique=True,blank=True)
	email = models.EmailField(unique=True)
	regist_time = models.DateTimeField(auto_now_add=True,null=True)
	password = models.CharField(max_length=128)

	def __init__(self,*args,**kwargs):
		for key,value in kwargs.items():
			if key == 'password':
				kwargs['password'] = make_password(value)
				break
		super(frontAuthModel,self).__init__(*args,**kwargs)

	def set_password(self,raw_password):
		self.password = make_password(raw_password)
		self.save(update_fields=['password'])

	def check_password(self,raw_password):
		if self.password == make_password(raw_password):
			return True
		else:
			return False


#注册用户相互关注模型
class authReationModel(models.Model):
	type = (
		('1','fans each othor'),
		('0','only i attenion you')
		)
	'''
	authA为关注者
	authB为被关注者
	relation_type为1代表双方互粉，代表单向关注
	'''
	authA = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='authAs')
	authB = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='authBs')
	relation_type = models.CharField(max_length=1,choices=type)