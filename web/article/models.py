from django.db import models
import uuid
from frontauth.models import frontAuthModel
# Create your models here.

#文章模型
class ArticleModel(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	title = models.CharField(max_length=200)
	content_html = models.TextField()
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,null=True)
	category = models.ForeignKey('CategoryModel',on_delete=models.CASCADE,null=True)
	release_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	read_count = models.IntegerField(null=True)
	tags = models.ManyToManyField('TagModel')
	top = models.OneToOneField('TopModel',on_delete=models.SET_NULL,null=True)

#分类模型
class CategoryModel(models.Model):
	name = models.CharField(max_length=50,unique=True)


#评论模型
class CommentModel(models.Model):
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	release_time = models.DateTimeField(auto_now_add=True)
	article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE)


#点赞/喜欢模型
class SupportModel(models.Model):
	status = {
		('1','support'),
		('0','give up support!')
	}
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE)
	article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE)
	status = models.CharField(max_length=1,choices=status)

class TagModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class TopModel(models.Model):
	top_time = models.DateTimeField(auto_now=True)