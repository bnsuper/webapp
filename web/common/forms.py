# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-30 09:32:33
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-30 09:32:58
from django import forms
from utils import bnjson

class BaseForm(forms.Form):
	def error_json_resopnse(self):
		error_dict = self.errors.as_data()
		# print(error_dict)
		message = ''
		for key in error_dict.keys():
			message = error_dict[key][0]
			break
		#将ValidationError中的字符串提取出来
		message = message.messages[0]
		return bnjson.json_params_error(message=message)