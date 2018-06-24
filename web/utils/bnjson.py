# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-22 10:58:12
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-22 11:37:59
from django.http import JsonResponse
from collections import namedtuple

HttpCode = namedtuple('Httpcode','ok paramserror')
httpcode = HttpCode(ok=200,paramserror=400)

def json_result(code=httpcode.ok,message='',data={},kwargs={}):
	json = {'code':code,'message':message,'data':data}
	if kwargs:
		for k,v in kwargs.items():
			json[k] = v
	return JsonResponse(json)

def json_params_error(message=''):
	'''
		参数错误
	'''
	return json_result(code=httpcode.paramserror,message=message)