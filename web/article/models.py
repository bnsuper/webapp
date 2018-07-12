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
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE)#评论人
	content = models.CharField(max_length=500)#评论内容
	release_time = models.DateTimeField(auto_now_add=True)#评论时间
	article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE)#评论文章

#评论回复模型
class CommentReplyModel(models.Model):
	comment = models.ForeignKey(CommentModel,on_delete=models.CASCADE) #评论
	reply_type = models.IntegerField() #回复类型，0表示回复评论，1表示回复评论的评论
	reply_id = models.IntegerField() #回复id，根据回复类型来决定，回复类型为0即为comment_id类型为1即为commentreply_id
	content = models.CharField(max_length=500)#评论内容
	from_author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='f_commentreply')#评论人
	to_author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE,related_name='to_commentreply')#被评论人

#点赞/喜欢模型
class SupportModel(models.Model):
	status = {
		('1','support'),
		('0','give up support!')
	}
	author = models.ForeignKey(frontAuthModel,on_delete=models.CASCADE)
	article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE,related_name='supports',related_query_name='supports')
	status = models.CharField(max_length=1,choices=status)

class TagModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class TopModel(models.Model):
	top_time = models.DateTimeField(auto_now=True)