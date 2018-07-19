# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-07-19 14:22:12
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-19 15:30:57
from django.http import HttpResponse
from utils.captcha.bncaptcha import Captcha
from io import BytesIO

def common_captcha(request):
	text,image = Captcha.gene_code()
	f = BytesIO()
	image.save(f,'png')
	f.seek(0)
	response = HttpResponse(content_type='image/png')
	response.write(f.read())
	f.close()
	return response
