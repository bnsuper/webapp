/*
* @Author: bn
* @Date:   2018-06-05 20:53:56
* @Last Modified by:   bn
* @Last Modified time: 2018-06-05 22:05:43
*/
'use strict'

$(function(){
	var url = window.location.href
	$('.menu-ul li').click(function(){
	$(this).addClass('active').siblings().removeClass('active')
	})
	// $('.menu-ul').children().eq(0).addClass('active').siblings().removeClass('active')
})