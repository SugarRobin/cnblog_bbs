// $(function () {
//    $('#add-board-btn').click(function (event) {
//        event.preventDefault();
//        xtalert.alertOneInput({
//            'text': '请输入板块名称',
//            'placeholder': '板块名称',
//            'confirmCallback': function (inputValue) {
//                bbsajax.post({
//                    'url': '/cms/aboard/',
//                    'data': {
//                        'name':inputValue
//                    },
//                    'success': function (data) {
//                        if(data['code'] ==200){
//                            window.location.reload();
//                        }else{
//                            xtalert.alertInfo(data['message'])
//                        }
//                    }
//                });
//            }
//        });
//    });
// });

// $(function () {
//     $('.input_boards_val1').click(function (event) {
//
//         var dialog = $("#banner-dialog2");
//         event.preventDefault();
//         var nameInput = dialog.find("input[name='input_boards_val']");
//         var name = nameInput.val();
//         console.log(name)
//
//
//     })
// })



//添加板块的js
$(function () {
   $('#add-board-btn').click(function (event) {
       event.preventDefault();
       // xtalert.alertOneInput({
       //     'text': '请输入板块名称',
       //     'placeholder': '板块名称',
       //     'confirmCallback': function (inputValue) {
       //
       //     }
       // });

       layer.prompt({title: '输入您要添加的板块，并确认', formType: 2}, function(text, index){


           bbsajax.post({
                   'url': '/cms/aboard/',
                   'data': {
                       'name':text
                   },
                   'success': function (data) {
                       if(data['code'] ==200){
                           layer.msg('添加成功')
                           window.location.reload();
                       }else{
                           // xtalert.alertInfo(data['message'])
                           layer.msg(data['message']);
                       }
                   }
               });


        layer.close(index);

    });



   });
});



// bbsajax.post({
//                    'url': '/cms/aboard/',
//                    'data': {
//                        'name':inputValue
//                    },
//                    'success': function (data) {
//                        if(data['code'] ==200){
//                            window.location.reload();
//                        }else{
//                            xtalert.alertInfo(data['message'])
//                        }
//                    }
//                });
//
//
// layer.prompt({title: '输入任何口令，并确认', formType: 1}, function(pass, index){
//   layer.close(index);
//   layer.prompt({title: '随便写点啥，并确认', formType: 2}, function(text, index){
//     layer.close(index);
//     layer.msg('演示完毕！您的口令：'+ pass +'<br>您最后写下了：'+text);
//   });
// });




//编辑板块
$(function () {
   $('.edit-board-btn').click(function () {
       var self = $(this);
       var tr = self.parent().parent();
       var name = tr.attr('data-name');
       var board_id = tr.attr('data-id');

       console.log(name,board_id)


       var txt;
        var person = prompt("请输入板块：", name);
        if (person == null || person == "") {
                 txt = "用户取消输入";
        } else {
                // console.log(txt)
            bbsajax.post({
                   'url': '/cms/uboard/',
                   'data': {
                       'board_id': board_id,
                       'name': person,
                   },
                   'success': function (data) {
                       if (data['code'] == 200) {
                           window.location.reload();
                       } else {
                           layer.msg(data['message'])
                       }
                   }
               });
            txt = "你好，" + person + "！今天过得好吗？";
            console.log('hello',name)
        }
        // document.getElementById("demo").innerHTML = txt;


       // xtalert.alertOneInput({
       //     'text': '请输入新板块名称',
       //     'placeholder': name,
       //     'confirmCallback': function (inputValue) {
       //         bbsajax.post({
       //             'url': '/cms/uboard/',
       //             'data': {
       //                 'board_id': board_id,
       //                 'name': inputValue
       //             },
       //             'success': function (data) {
       //                 if (data['code'] == 200) {
       //                     window.location.reload();
       //                 } else {
       //                     xtalert.alertInfo(data['message'])
       //                 }
       //             }
       //         });
       //     }
       // });
   })
});


//删除板块
$(function () {
   $('.delete-board-btn').click(function () {
       var self = $(this);
       var tr = self.parent().parent();
       var board_id = tr.attr('data-id');

       bbsajax.post({
           'url': '/cms/dboard/',
           'data': {
               'board_id': board_id
           },
           'success': function (data) {
               if (data['code'] == 200) {
                   window.location.reload();
               } else {
                   // xtalert.alertInfo(data['message'])
                   layer.msg(data['message'])
               }
           }
       });
   });
});
