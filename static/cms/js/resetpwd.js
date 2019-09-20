

$(function () {
    $('#submit').click(function (event) {

        // layer.msg('hello');
        //阻止按钮默认的提交表单行为
        event.preventDefault();
        var oldpwdE = $('input[name=oldpwd]');
        var newpwdE = $('input[name=newpwd]');
        var newpwd2E = $('input[name=newpwd2]');

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //这里使用我们自己封装好的bbsajax，它具有了csrf
        bbsajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                if(data['code'] === 200){
                     layer.msg(data['message'])
                    oldpwdE.val('');   //完成请求后把表单输入的值清空
                    newpwdE.val('');
                    newpwd2E.val('');
                }else {
                   layer.msg('错误:'+data['message'])
                //     layer.open({
                //       type: 1,
                //       skin: 'layui-layer-demo', //样式类名
                //       closeBtn: 0, //不显示关闭按钮
                //       anim: 2,
                //       shadeClose: true, //开启遮罩关闭
                //       content: data['message']
                // });

                oldpwdE.val('');   //完成请求后把表单输入的值清空
                    newpwdE.val('');
                    newpwd2E.val('');
                }
                console.log(data);


            },
            'fail': function (error) {


                 layer.msg('网络错误')
                console.log(error);

            }
        });
    });
})
