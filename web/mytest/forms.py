# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-01 10:43:09
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-01 15:23:43
from django import forms
from .models import STATUS_CHOICES,testb_Model


class testForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=20)
	email = forms.URLField(label='邮箱')
	password = forms.CharField(label='密码',min_length=6)
	status = forms.CharField(label='状态',min_length=1,max_length=1,widget=forms.Select(choices=STATUS_CHOICES))

# class test_Model(models.Model):
# 	username = models.CharField(max_length=20,unique=True)
# 	email = models.EmailField(default='oop@qq.com')
# 	password = models.CharField(max_length=20)
# 	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='d')

class testbForm(forms.ModelForm):
	class Meta:
		model = testb_Model
		fields = '__all__'
