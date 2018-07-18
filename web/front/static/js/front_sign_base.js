

$(function(){
	var url = window.location.href
	var number = url.indexOf('signin')
	var index = 0
	if(url.indexOf('sign_in') > 0){
		$(".normal-title a").eq(index).addClass('active-cus')

	}
	else if(url.indexOf('sign_up') > 0){
		index = index + 1
		$(".normal-title a").eq(index).addClass('active-cus')
	}

})