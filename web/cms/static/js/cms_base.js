/*
* @Author: bn
* @Date:   2018-06-05 20:53:56
* @Last Modified by:   bn
* @Last Modified time: 2018-06-24 23:00:15
*/
'use strict'

$(function(){
	// var url = window.location.href
	// $('.menu-ul li').click(function(){
	// $(this).addClass('active').siblings().removeClass('active')
	// })
	var url = window.location.href;
	var index = 0;
	if (url.indexOf('authors') >= 0) 
	{
			index = 0;
			console.log('comming!');
			console.log(index)
			$('.menu-ul').children().eq(index).addClass('active').siblings().removeClass('active');

	} 
	else if(url.indexOf('article') >= 0)
	{
			index = 1;
			console.log('article manager comming!');
			$('.menu-ul').children().eq(index).addClass('active').siblings().removeClass('active');

	}
	else 
	{
		$('.menu-ul').children().eq(index).addClass('active').siblings().removeClass('active');
	}
})