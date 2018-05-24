from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class test_Model(models.Model):
	username = models.CharField(max_length=20,unique=True)
	email = models.EmailField(default='oop@qq.com')
	password = models.CharField(max_length=20)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='d')

	def __str__(self):
		return self.username