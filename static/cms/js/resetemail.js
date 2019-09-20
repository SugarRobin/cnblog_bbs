$(function () {
    $('#get_captcha').click(function (event) {
        event.preventDefault();
        var email = $('input[name=email]').val();
        if(!email){
            layer.msg('请输入邮箱');
            return;
        }

        bbsajax.get({

            'url':'/cms/email_captcha/',
            'data':{
                'email':email
            },

            'success':function (data) {
                if (data['code'] === 200){
                    layer.msg(data['message']);

                }else {
                    layer.msg(data['message']);
                }

            },

            'fail':function (error) {
                layer.msg('网络错误');

            }
        })


    })

    // $('#submit').click(function (event) {
    //     console.log('dsafl;');
    //     event.preventDefault();
    //     var emailE = $('input[name=email]');
    //     var captchaE = $('input[name=captcha]');
    //
    //     var email = emailE.val();
    //     var captcha = captchaE.val();
    //
    //     console.log('邮箱的值为:'+email)
    //     console.log('验证码的值为:'+captcha)
    //
    //     bbsajax.post({
    //
    //         'url':'/cms/resetemail/',
    //         'data':{
    //             'email':email,
    //             'captcha':captcha
    //         },
    //
    //         'success':function (data) {
    //             if(data['code'] === 200){
    //                 layer.msg(data['message']);
    //                 emailE.val('');
    //                 captchaE.val();
    //             }else {
    //                 layer.msg('修改失败:'+data['message']);
    //             }
    //
    //         },
    //         'fail':function (error) {
    //             layer.msg('网络错误');
    //
    //         }
    //     })
    //
    // })

});

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var emailE = $('input[name=email]');
        var captchaE = $('input[name=captcha]');

        var email = emailE.val();
        var captcha = captchaE.val();

        bbsajax.post({
            'url': '/cms/resetemail/',
            'data': {
                'email': email,
                'captcha': captcha
            },
            'success': function (data) {
                if (data['code'] === 200){
                    layer.msg(data['message']);
                    emailE.val('');
                    captchaE.val('');
                }else{
                   layer.msg('修改失败:'+data['message']);
                }
            },
            'fail': function (error) {
               layer.msg('网络错误');
            }
        })
    })
});
