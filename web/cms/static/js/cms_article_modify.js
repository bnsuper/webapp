/*
* @Author: chenbin
* @Date:   2018-06-28 09:49:46
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-29 15:45:24
*/

// 初始化simditor编辑器
$(function(){
	var editor = new Simditor({
	  textarea: $('#editor')
	});
})

// 绑定添加分类的点击事件，调出模态框，用ajax传递数据等
$(function(){
	var dialog = $('#add-category-modal')
	$('.add-category-btn').click(function(){
		dialog.modal('show');
	});
	$('.category-submit').click(function(){
		var name = $('.category-input').val()
		console.log(name)
		bnajax.post({
			url: '/cms/article/add_category/',
			data: {
				name:name
			},
			success: function(data){
				if(data.code == 200){
					var Data = data.data
					var id = Data.id
					var name = Data.name
					console.log(id+'--'+name)
					var data = {
						id: id,
						name: name
					}
					var html = bntemplate.template('category',data)
					$('.category-select').append(html)
					$('.category-select option').removeAttr("selected").last().attr("selected","selected")
					dialog.modal('hide')
				}
				else{
					var message = data.message
					alert(message)
				}
			},
			error: function(err){
				alert(err)
			}
		})
	})
})


// 绑定添加标签的点击事件，调出模态框，用ajax传递数据等
$(function(){
	var dialog = $('#add-tag-modal')
	$('.add-tag-btn').click(function(){
		dialog.modal('show')
	})
	$('.tag-submit').click(function(){
	var name = $('.tag-input').val()
	console.log(name)
	bnajax.post({
		url: '/cms/article/add_tag/',
		data: {
			name:name
		},
		success: function(data){
			if(data.code == 200){
				var Data = data.data
				var id = Data.id
				var name = Data.name
				console.log(id+'--'+name)
				var data = {
					id: id,
					name: name
				}
				var html = bntemplate.template('tag',data)
				$('.tag-div').append(html)
				dialog.modal('hide')
			}
			else{
				var message = data.message
				if (typeof message == 'object'){
					for(var key in message){
						message = message[key][0]
						break
					}
				}
				alert(message)
			}
		},
		error: function(err){
			alert(err)
		}
	})
})

})
