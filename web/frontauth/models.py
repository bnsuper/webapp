from django.db import models
import uuid
# Create your models here.

class frontAuthModel(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	username = models.CharField(max_length=20,unique=True)
	tel = models.CharField(max_length=20,unique=True,blank=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=128)

	def set_password(self,raw_password):
		pass

	def check_password(self,raw_password):
		pass

	#make_password()