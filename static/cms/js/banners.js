// $(function () {
//     $("#save-banner-btn").click(function (event) {
//         event.preventDefault();
//         var dialog = $("#banner-dialog");
//         var nameInput = dialog.find("input[name='name']");
//         var imageInput = dialog.find("input[name='image_url']");
//         var linkInput = dialog.find("input[name='link_url']");
//         var priorityInput = dialog.find("input[name='priority']");
//
//         var name = nameInput.val();
//         var image_url = imageInput.val();
//         var link_url = linkInput.val();
//         var priority = priorityInput.val();
//
//         if(!name || !image_url || !link_url || !priority){
//             // zlalert.alertInfoToast('请输入完整的轮播图数据！');
//             layer.msg('请输入完整的轮播图数据！');
//             return;
//         }
//
//         bbsajax.post({
//             "url": '/cms/abanner/',
//             "data": {
//                 'name':name,
//                 'image_url': image_url,
//                 'link_url': link_url,
//                 'priority':priority,
//             },
//             'success': function (data) {
//                 dialog.modal("hide");
//                 if(data['code'] == 200){
//                     // 重新加载这个页面
//                     window.location.reload();
//                 }else{
//                     // zlalert.alertInfo(data['message']);
//                     layer.msg('提交失败:'+data['message']);
//                 }
//             },
//             'fail': function () {
//                 // zlalert.alertNetworkError();
//                 layer.msg('网络错误');
//             }
//
//         });
//     });
// });
//

//编辑
$(function () {
    $("#save-banner-btn1").click(function (event) {
        event.preventDefault();
        self = $(this);
        var dialog = $("#banner-dialog1");
        var nameInput = dialog.find("input[name='name']");
        var imageInput = dialog.find("input[name='image_url']");
        var linkInput = dialog.find("input[name='link_url']");
        var priorityInput = dialog.find("input[name='priority']");

        var name = nameInput.val();
        var image_url = imageInput.val();
        var link_url = linkInput.val();
        var priority = priorityInput.val();
        //通过保存按钮上的属性data-type，获取数据类型，如果它的值是update,就是编辑操作了，否则就是添加操作
        var submitType = self.attr('data-type');
        console.log(submitType)
        console.log('djafjndsvnann;12334456777')
        //这里通过保存按钮上的属性data-id获取到轮播图的id, 如果是添加轮播图这就是个空值，不用管它
        var bannerId = self.attr("data-id");

        if(!name || !image_url || !link_url || !priority){
            // zlalert.alertInfoToast('请输入完整的轮播图数据！');
            layer.msg('请输入完整的轮播图');

            return;
        }

        //根据submitType的值来判断url应该是添加还是编辑
        var url = '';
        if(submitType == 'update'){
            url = '/cms/ubanner/';
        }else{
            url = '/cms/abanner/';
        }

        bbsajax.post({
            "url": url,   //这里就要改成动态获取上面的url了
            "data": {
                'name':name,
                'image_url': image_url,
                'link_url': link_url,
                'priority':priority,
                'banner_id': bannerId    //这里需要多传入一个轮播图id，就是是添加操作也无所谓，后端也没接收
            },
            'success': function (data) {
                dialog.modal("hide");
                if(data['code'] == 200){
                    // 重新加载这个页面
                    window.location.reload();
                }else{
                    // zlalert.alertInfo(data['message']);
                    layer.msg('提交失败:'+data['message']);
                }
            },
            'fail': function () {
                // zlalert.alertNetworkError();
                layer.msg('网络错误');
            }

        });
    });
});





$(function () {
    bbsqiniu.setUp({
        // 'domain':'http://pxwttml1j.bkt.clouddn.com',  //七牛的域名
        'domain':'http://pyb9vndqb.bkt.clouddn.com/',
        'browse_btn':'upload-btn',    //按钮的id
        'uptoken_url':'http://127.0.0.1:5000/cms/uptoken/',     //后端的url获取token
        'success':function (up,file,info) {
            var imageInput = $("input[name='image_url']");
            imageInput.val(file.name);      //把图片的完整地址填入到表单中

        }
    })

})


console.log('12337478893589')

$(function () {
    $(".delete-banner-btn1").click(function (event) {
        console.log('deleteeeeeeeeeeeeeee')
        var self = $(this);
        var tr = self.parent().parent();
        var banner_id = tr.attr('data-id');
        // xtalert.alertConfirm({
        //     "msg":"您确定要删除这个轮播图吗？",
        //     'confirmCallback': function () {
        //         bbsajax.post({
        //             'url': '/cms/dbanner/',
        //             'data':{
        //                 'banner_id': banner_id
        //             },
        //             'success': function (data) {
        //                 if(data['code'] == 200){
        //                     window.location.reload();
        //                 }else{
        //                     // xtalert.alertInfo(data['message']);
        //
        //                 }
        //             }
        //         })
        //     }
        // });

        layer.confirm('您是确定要删除这条轮播图么？', {

            btn: ['确定','取消'] //按钮
                }, function(){

                    bbsajax.post({
                    'url': '/cms/dbanner/',
                    'data':{
                        'banner_id': banner_id
                    },
                    'success': function (data) {
                        if(data['code'] == 200){
                            layer.msg('删除成功', {icon: 3});
                            window.location.reload();
                            layer.msg('删除成功', {icon: 3});
                        }else{
                            // xtalert.alertInfo(data['message']);
                            layer.msg('的确很重要', {icon: 1});


                        }

                        layer.msg('删除成功', {icon: 1});

                    }
                })


                }, function(){
                  layer.msg('取消删除', {
                    time: 5000, //20s后自动关闭
                    // btn: ['明白了', '知道了']


                  });
        });




    });
});
