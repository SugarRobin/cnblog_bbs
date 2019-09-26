$(function () {
    var ue = UE.getEditor("editor",{
        "serverUrl": '/ueditor/upload/'
    });

    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $('input[name="title"]');
        var boardSelect = $("select[name='board_id']");

        var title = titleInput.val();
        var board_id = boardSelect.val();
        var content = ue.getContent();

        bbsajax.post({
            'url': '/apost/',
            'data': {
                'title': title,
                'content':content,
                'board_id': board_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    // xtalert.alertConfirm({
                    //     'msg': '恭喜！帖子发表成功！',
                    //     'cancelText': '回到首页',
                    //     'confirmText': '再发一篇',
                    //     'cancelCallback': function () {
                    //         window.location = '/';
                    //     },
                    //     'confirmCallback': function () {
                    //         titleInput.val("");
                    //         ue.setContent("");
                    //     }
                    // });
                    layer.confirm('恭喜！帖子发表成功！！！', {
                          btn: ['回到首页','在发一篇'] //按钮
                        }, function(){
                            window.location = '/';


                          layer.msg('的确很重要', {icon: 1});
                        }, function(){
                          // layer.msg('也可以这样', {
                          //   time: 20000, //20s后自动关闭
                          //   btn: ['明白了', '知道了']
                          // });
                                titleInput.val("");
                                ue.setContent("");

                        });


                    console.log('sucess')
                }else{
                    // xtalert.alertInfo(data['message']);
                    console.log('faild')
                }
            }
        });
    });
});
