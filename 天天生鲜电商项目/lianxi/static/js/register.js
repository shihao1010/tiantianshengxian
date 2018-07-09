$(function(){			//$(function()){}等价于$(document).ready(function(){})
						//这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码。
	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;

	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {      //绑定点击事件
		if($(this).is(':checked'))      //:checked返回封装了所有选中的表单域元素的jQuery对象。
		{                               //如果找不到任何相应的匹配，则返回一个空的jQuery对象。
			error_check = false;
			$(this).siblings('span').hide();    //查找每个allow元素的所有标签为 "span" 的所有同胞元素：
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			$.get('/user/register_exist/?uname='+$('#user_name').val(), function (data) {
				if (data.count == 1){
					$('#user_name').next().html('用户名已存在').show();
					error_name = true;
				} else {
					$('#user_name').next().hide();
					error_name = false;
				}
            });
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位');
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))      //test() 方法用于检测一个字符串是否匹配某个模式.
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确');
			$('#email').next().show();
			error_email = true;
		}
	}

	$('#zhuce').click(function() {      //提交按钮,所有验证通过方可提交
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
		    $('#zhuceform').submit();   //提交表单
			return true;
		}
		else
		{
		    console.log('输入有误');     //在控制台输出
			return false;
		}
	})
})
