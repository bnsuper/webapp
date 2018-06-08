# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-08 15:52:22
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-08 16:07:04

from django.conf import settings
from random import randint

#生成author列表，对应frontAuthModel模型，number是生成的数量
def makeAuthors(number):
	author_list = []
	for i in range(number):
	#随机生成姓名
		begin_name = settings.BEGIN_NAME
		counta = len(begin_name)
		end_name = settings.END_NAME
		countb = len(end_name)
		username = begin_name[randint(0,counta-1)] + end_name[randint(0,countb-1)]
		print('姓名：',username)
		#随机生成电话
		begin_tel = ['132','186']
		count = len(begin_tel)
		end_tel = ''
		for x in range(8):
			end_tel += str(randint(0,9))
		tel = begin_tel[randint(0,count-1)] + end_tel
		print('电话：',tel)
		#随机生成邮箱
		end_email = ['@qq.com','@163.com','@sina.com','@sohu.com']
		begin_email = ''
		count = len(end_email)
		sure_end_email = end_email[randint(0,count-1)]
		N = randint(6,15)
		n = randint(0,N)
		temp = randint(0,1)
		for y in range(N):
			if sure_end_email == '@qq.com':
				begin_email += chr(randint(48,57))
			else:
				if temp == 1:
					if y <= n:
						begin_email += chr(randint(97,122))
					else:
						begin_email += chr(randint(48,57))
				else:
					if y > n:
						begin_email += chr(randint(97,122))
					else:
						begin_email += chr(randint(48,57))
		email = begin_email + sure_end_email
		print('email:',email)
		kwargs = {'username':username,'tel':tel,'email':email,'password':'123456'}
		author_list.append(kwargs)
	return author_list