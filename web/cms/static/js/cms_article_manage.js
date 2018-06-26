/*
* @Author: chenbin
* @Date:   2018-06-11 11:58:59
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-26 18:07:16
*/

var art = function(data){
		// console.log(data)
		var c_page = data.data.c_page
		var pages = data.data.pages
		var all_pages = data.data.all_pages
		var p_data = {
			c_page: c_page,
			pages: pages,
			all_pages: all_pages
		}
		var Page = bntemplate.template('page',p_data)
		$('.page-col').html(Page)

		var articles = data.data.article
		var a_data = {
			articles: articles
		}
		var Article = bntemplate.template('article',a_data)
		$('.article-tbody').html(Article)
}

var f = $(function(){
		var title = $("input[name='title']").val()
		var author = $("input[name='author']").val()
		var category = $("input[name='category']").val()
		bnajax.post({
			url:'/cms/article/query/',
			data:{
				'title':title,
				'author':author,
				'category':category,
				'c_page': '1'
			},
			success:function(data){
				art(data)
			},	
			error:function(err){
				alert(err)
			},
			complete:function(){
				console.log('ajax is completed')
				console.log($('.page-a'))
				// $('.page-a').click(function(event){
				// 	event.preventDefault();
				// 	console.log('hello world!')
				// 	var title = $("input[name='title']").val()
				// 	var author = $("input[name='author']").val()
				// 	var category = $("input[name='category']").val()
				// 	var c_page = $(this).attr('page')
				// 	console.log(c_page)
				// 	bnajax.post({
				// 		url:'/cms/article/query/',
				// 		data:{
				// 			'title':title,
				// 			'author':author,
				// 			'category':category,
				// 			'c_page': c_page
				// 		},
				// 		success:function(data){
				// 			art(data)
				// 		},
				// 		error:function(err){
				// 			alert(err)
				// 		},
				// 		complete:function(){
				// 			console.log('welcome!')
				// 		}
				// 	})
				// });

			}
		})
})

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
				'category':category,
				'c_page': '1'
			},
			success:function(data){
				art(data)
			},
			error:function(err){
				alert(err)
			},
			complete:function(){
				console.log('ajax is completed')
				var x = $('.page-a')
				console.log(x)
			}
		})

	});
})

	// $('.pagination').delegate('a','f',function(event){
	// 	event.preventDefault()

	// })







$(function(){
	console.log($('.pagination'));
	// $('.page-a').live("click",function(event){
	// 	event.preventDefault();
	// 	console.log('commint nice nice')
	// 	var title = $("input[name='title']").val()
	// 	var author = $("input[name='author']").val()
	// 	var category = $("input[name='category']").val()
	// 	var c_page = $(this).attr('name')
	// 	bnajax.post({
	// 		url:'/cms/article/query/',
	// 		data:{
	// 			'title':title,
	// 			'author':author,
	// 			'category':category,
	// 			'c_page': c_page
	// 		},
	// 		success:function(data){
	// 			art(data)
	// 		},
	// 		error:function(err){
	// 			alert(err)
	// 		},
	// 		complete:function(){
	// 			console.log('ajax is completed')
	// 		}
	// 	})
	// })
	$('.pagination').on("click","li a",function(event){  
		    event.preventDefault();
			console.log('commint nice nice')
			var title = $("input[name='title']").val()
			var author = $("input[name='author']").val()
			var category = $("input[name='category']").val()
			var c_page = $(this).attr('name')
			bnajax.post({
				url:'/cms/article/query/',
				data:{
					'title':title,
					'author':author,
					'category':category,
					'c_page': c_page
				},
				success:function(data){
					art(data)
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


	
