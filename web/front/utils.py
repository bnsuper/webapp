# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-07-09 10:59:24
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-09 15:32:45

#前台页面加载更多的分页功能
Article_count = 10  #单页的文章展示数量
def page(current_page,query_result,query_name):
	#count指文章或者注册用户数量
	count = len(query_result)
	#当前页展示的用户或者文章数量
	c_articles = Article_count
	#当前页
	c_page = int(current_page)
	#切片开始和结束的位置
	end = c_page*c_articles
	begin = end - c_articles
	query_dice = query_result[begin:end]
	context = {
		'c_page': c_page,
		 query_name: query_dice
	}
	return context