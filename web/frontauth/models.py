from django.db import models
import uuid
# Create your models here.

#注册用户模型
class frontAuthModel(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	username = models.CharField(max_length=20,unique=True)
	tel = models.CharField(max_length=20,unique=True,blank=True)
	email = models.EmailField(unique=True)
	regist_time = models.DateTimeField(auto_now_add=True,null=True)
	password = models.CharField(max_length=128)

	def set_password(self,raw_password):
		pass

	def check_password(self,raw_password):
		pass

	#make_password()

#注册用户相互关注模型
class authReationModel(models.Model):
	type = (
		('1','attention'),
		('2','fans')
		)
	authA = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='authAs')
	authB = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='authBs')
	relation_type = models.CharField(max_length=1,choices=type)