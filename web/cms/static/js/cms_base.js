/*
* @Author: bn
* @Date:   2018-06-05 20:53:56
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-08 10:09:07
*/
'use strict'

$(function(){
	// var url = window.location.href
	// $('.menu-ul li').click(function(){
	// $(this).addClass('active').siblings().removeClass('active')
	// })
	var url = window.location.href
	var index = 0
	if (url.indexOf('authors') >= 0) 
	{
		console.log('comming!')
		$('.menu-ul').children().eq(index).addClass('active').siblings().removeClass('active')
	} 
	else 
	{
		$('.menu-ul').children().eq(index).addClass('active').siblings().removeClass('active')
	}
})