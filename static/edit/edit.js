$(function(){
  $("#btn_preview").click(function(){
            $("#actionform").attr("action","/preview");
            $("#actionform").submit();
            });
          });
$().ready(function() {
	// validate signup form on keyup and submit
	$("#actionform").validate({
		rules: {
			title: "required",
			brief: "required",
			content: "required"
		},
		messages: {
			title: "请输入标题",
			brief: "请输入摘要",
			content:"请输入内容"
		}
	});
$("#reqFile").uploadify({
            'uploader' :  '/static/upload/uploadify.swf' ,
            'script' : "/file?_xsrf="+$('[name=_xsrf]').val(),
            'cancelImg' : '/static/upload/cancel.png',
            'auto' : true,
            'fileExt' : '.doc',
            'fileDesc' : '请选择png文件',
            'fileDataName' : 'reqFile',
            'buttonImg' :'/static/images/upload_btn.jpg',
            'width' : '80',
            'height' : '26',
            'queueID' : "upFileList",
            'onComplete' : function(event, queueId, fileObj, response, data) {

            }
});

});