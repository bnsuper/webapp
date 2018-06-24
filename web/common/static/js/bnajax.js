/*
* @Author: chenbin
* @Date:   2018-06-22 15:01:32
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-22 15:40:49
*/
function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

var bnajax = {
	post:function(args){
		args['type'] = 'POST';
		this.ajax(args)
	},
	get:function(args){
		args['type'] = 'GET';
		this.ajax(args)
	},
	ajax:function(settings){
		this._beforSend();
		$.ajax(settings)
	},
	_beforSend:function(){
		$.ajaxSetup({
			beforSend:function(xhr,settings){
				 if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            		xhr.setRequestHeader("X-CSRFToken", csrftoken);
        				}
			}
		})
	}
}