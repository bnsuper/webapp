from django.db import models
import uuid
from frontauth.models import frontAuthModel
# Create your models here.

class ArticleModel(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	title = models.CharField(max_length=200)
	content_html = models.TextField()
	category = models.ForeignKey('CategoryModel',on_delete=models.CASCADE)
	release_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	read_count = models.IntegerField()




class CategoryModel(models.Model):
	name = models.CharField(max_length=50)


class CommentModel(models.Model):
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	release_time = models.DateTimeField(auto_now_add=True)
	article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE)


