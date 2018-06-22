/*
* @Author: chenbin
* @Date:   2018-06-05 18:03:28
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-22 17:16:57
*/
// $(function(){
// 	$('.btn-delete').click(function(event){
// 		event.preventDefault();
// 		console.log(this)
// 	});
// })

$(function(){
	$('.auth-delete').click(function(event){
		event.preventDefault();
		var c_url = window.location.href
		var uid = $(this).parent().parent().attr('uid')
		var r = confirm('您确定要删除该用户吗')
		if(r == true){
					bnajax.post({
			url:'/cms/authors/delete/',
			data:{
				author_uid:uid
			},
			success:function(data){
				console.log('用户被删除')
			},
			error:function(error){
				alert(error)
			},
			complete:function(){
				window.location.href = c_url
			}
			})
		}

	})
})