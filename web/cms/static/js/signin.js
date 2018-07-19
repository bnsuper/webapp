/*
* @Author: chenbin
* @Date:   2018-07-19 15:53:02
* @Last Modified by:   chenbin
* @Last Modified time: 2018-07-19 16:23:38
*/
$(function(){
	$('.a-captha').click(function(event){
		event.preventDefault();
		var temp = $(this).children().eq(0);
		var url = temp.attr('src');
		var str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		var n = 4, s = "";
		for(var i = 0; i < n; i++){
		    var rand = Math.floor(Math.random() * str.length);
		    s += str.charAt(rand);
		}
		if (url.indexOf('?') > 0){
			url = url + s
			temp.attr('src',url)
		}
		else{
			url = url + "?q=" + s
			temp.attr('src',url)
		}
	})
})