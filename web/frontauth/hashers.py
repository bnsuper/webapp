# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-06 11:21:58
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-08 18:05:13

def make_password(password,slt=None,hasher='default'):
	if password is None:
		return None
	