/*
* @Author: chenbin
* @Date:   2018-07-09 15:11:50
* @Last Modified by:   bn
* @Last Modified time: 2018-07-12 20:50:30
*/

function checkHtml(htmlStr) {
    var  reg = /<[^>]+>/g;
    return reg.test(htmlStr);
}

$(function(){
	$('#read-more').on('click',function(){
		var self = $(this)
		self.button('loading')
		var c_page = self.attr('current-page')
		bnajax.get({
			url:'/',
			data:{
				c_page: c_page,
			},
			success:function(data){
				if(data['code'] == 200){
					console.log(data)
					var data = data.data
					var c_page = data.c_page
					var article_data = data.untop_articles
					if(article_data.length==0){
						console.log(c_page)
						self.text('没有更多文章了')
					}
					else{
						for(var i=0;i < article_data.length; i++){
							var article = article_data[i]
							var content_html = article['content_html']
							if(checkHtml(content_html)){
								content_html = $(content_html).text()
							}
							if(content_html.length > 70){
								content_html = content_html.substr(0,70) + '...';
							}
							article['content_html'] = content_html
						}
						var articles = {
						articles: article_data
						}
						console.log(c_page)
						console.log(articles)
						var Articles = bntemplate.template('readmore',articles)
						$('.note-list').append(Articles)
						self.attr('current-page',c_page+1)
						self.button('reset')
					}
					
				}
				else{
					alert(data['message'])
				}
			},	
			error:function(err){
				alert(err)

			},
			complete:function(){
				
			}
		})
	})
})