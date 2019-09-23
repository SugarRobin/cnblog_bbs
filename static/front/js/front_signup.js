$(function(){
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var newsrc = bbsparam.setParam(src,'xx',Math.random());
        self.attr('src',newsrc);
    });
});


//发送手机验证码
$(function () {
    $("#sms-captcha-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var telephone = $("input[name='telephone']").val();
        if(!(/^1[345879]\d{9}$/.test(telephone))){
           layer.msg('请输入正确的手机号码！');
            return;
        }
        var timestamp = (new Date).getTime();
        var sign = hex_md5(timestamp+telephone+"fgeWdLwg436t@$%$^"); //这里用到的hex_md5需要导入另外一个js
        bbsajax.post({
            'url': '/c/sms_captcha/',
            'data':{
                'telephone': telephone,
                'timestamp': timestamp,
                'sign': sign
            },
            'success': function (data) {
                if(data['code'] == 200){
                    // xtalert.alertSuccessToast(data['message']);
                    layer.msg(data['message'])
                    self.attr("disabled",'disabled');
                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;
                        self.text(timeCount);
                        if(timeCount <= 0){
                            self.removeAttr('disabled');
                            clearInterval(timer);
                            self.text('发送验证码');
                        }
                    },1000);
                }else{
                    // xtalert.alertInfoToast(data['message']);
                    layer.msg(data['message']);
                }
            }
        });
    });
});


$(function () {
    $('#submit-btn').click(function (event) {
        console.log(1)
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var sms_captcha_input = $("input[name='sms_captcha']");
        var username_input = $("input[name='username']");
        var password1_input = $("input[name='password1']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']")

        var telephone = telephone_input.val();
        var sms_captcha = sms_captcha_input.val();
        var username = username_input.val();
        var password1 = password1_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        console.log('用户验证码:',sms_captcha_input)

        bbsajax.post({
            'url': '/signup/',
            'data': {
                'telephone': telephone,
                'sms_captcha': sms_captcha,
                'username': username,
                'password1': password1,
                'password2': password2,
                'graph_captcha': graph_captcha
            },
            'success': function (data) {
                if (data['code'] === 200){
                    //注册成功跳转到首页
                    // window.location = '/';
                    var return_to = $("#return-to-span").text();
                    if(return_to){
                        window.location = return_to;

                    }else {
                        window.location = '/'
                    }
                }else{
                    // xtalert.alertInfo(data['message']);
                    layer.msg(data['message'])
                }
            },
            'fail': function (error) {
                // xtalert.alertNetworkError();
                layer.msg('网络错误，请重试')

            }

        });
    })
});
