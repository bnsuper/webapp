/*
* @Author: chenbin
* @Date:   2018-06-11 11:58:59
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-25 16:53:15
*/
$(function(){
	$('.query-btn').click(function(event){
		event.preventDefault();
		var title = $("input[name='title']").val()
		var author = $("input[name='author']").val()
		var category = $("input[name='category']").val()
		bnajax.post({
			url:'/cms/article/query/',
			data:{
				'title':title,
				'author':author,
				'category':category
			},
			success:function(data){
				console.log(data)
			},
			error:function(err){
				alert(err)
			},
			complete:function(){
				console.log('ajax is completed')
			}
		})
	});
})