/*
* @Author: chenbin
* @Date:   2018-06-26 14:47:49
* @Last Modified by:   chenbin
* @Last Modified time: 2018-06-26 15:25:02
*/
var bntemplate = {
	'template': function(id,data) {
		// 先添加格式化时间的辅助函数
		template.defaults.imports.dateFormat = this._dateFormat
		// helper在此处不存在改函数，https://segmentfault.com/q/1010000009712447
		// template.helper('dateFormat',this._dateFormat);
		return template(id,data);
	},
	'_dateFormat': function (date, format) {
	    date = new Date(date);
	    var map = {
	        "M": date.getMonth() + 1, //月份 
	        "d": date.getDate(), //日 
	        "h": date.getHours(), //小时 
	        "m": date.getMinutes(), //分 
	        "s": date.getSeconds(), //秒 
	        "q": Math.floor((date.getMonth() + 3) / 3), //季度 
	        "S": date.getMilliseconds() //毫秒 
	    };
	    format = format.replace(/([yMdhmsqS])+/g, function(all, t){
	        var v = map[t];
	        if(v !== undefined){
	            if(all.length > 1){
	                v = '0' + v;
	                v = v.substr(v.length-2);
	            }
	            return v;
	        }
	        else if(t === 'y'){
	            return (date.getFullYear() + '').substr(4 - all.length);
	        }
	        return all;
	    });
	    return format;
	}
}