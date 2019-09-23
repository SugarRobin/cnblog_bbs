from flask import Blueprint,make_response,request
from utils.captcha import Captcha
from io import BytesIO
import json
from utils import xcache

from utils.zzy_cms.zhenzismsclient import send_sms
from utils import xjson
from .forms import SmsCaptchaForm
from flask import jsonify
import qiniu

bp = Blueprint('common',__name__,url_prefix='/c')


@bp.route('/')
def index():
    return 'common  index'



@bp.route('/graph_captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    xcache.set(text.lower(),text.lower()) #图片验证码这里，不好设置一个唯一的key,索性直接也用验证码的值作为key
    return resp


# @bp.route('/sms_captcha/')
# def sms_captcha():
#     telephone = request.args.get('telephone')
#     cont = '您正在注册bbs论,坛验证码为：%s,如无此需求，请无视此需求' %('520')
#     params = {'code':cont}
#     result = send_sms(telephone,params)
#     dict_res = json.loads(result)
#     if dict_res['code'] == 0:
#         return '发送成功'
#     else:
#         return '发送失败'
#     return result

@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    sms_captcha_form = SmsCaptchaForm(request.form)
    if sms_captcha_form.validate():
        telephone = sms_captcha_form.telephone.data
        #生成随机的验证，之前图片那里有方法实现了，我们直接调用就行，生成6位的验证码
        radom_code = Captcha.gene_text(6)
        cont = '测试bbs,您的验证码为：%s' % (radom_code)
        params = {'code': cont}
        result = send_sms(telephone, params)
        dict_res = json.loads(result)
        if dict_res['code'] == 0:
            xcache.set(telephone,radom_code) #把手机号作为key
            return xjson.json_sucess('短信发送成功')
        else:
            return xjson.json_server_error('短信发送失败')
    else:
        return xjson.json_params_error('参数错误')


@bp.route('/uptoken/')
def uptoken():
    access_key = ''
    secret_key = ''
























