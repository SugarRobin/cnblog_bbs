from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp,Length,EqualTo,ValidationError
from utils import xcache
from .models import FrontUser


class SignUpForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[35678]\d{9}', message='手机号码格式错误')])
    sms_captcha = StringField(validators=[Regexp(r'\w{6}', message='短信验证码错误')])
    username = StringField(validators=[Length(2,20, message='用户名格式错误')])
    password1 = StringField(validators=[Length(5, 30, message='密码格式错误')])
    password2 = StringField(validators=[EqualTo('password1', message='两次密码不一致')])
    graph_captcha = StringField(validators=[Regexp(r'\w{4}', message='图形验证码错误')])

    def validate_telephone(self, field):
        user = FrontUser.query.filter_by(telephone=field.data).first()
        if user:
            raise ValidationError('该手机号已被注册')

    def validate_sms_captcha(self, field):
        telephone = self.telephone.data
        sms_captcha = field.data
        xcache.set('13602219337', 'heboan')
        sms_captcha_mem = xcache.get(telephone)
        print('用户输入的验证码：{}'.format(sms_captcha))
        print( '服务器存储的验证码：{}'.format(sms_captcha_mem))
        if not sms_captcha_mem or sms_captcha_mem != sms_captcha:
            raise ValidationError(message='短信验证码错误')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        #因为图形验证码存储的key和值都是一样的，所以我们只要判断key是否存在就行
        if not xcache.get(graph_captcha.lower()):
            raise ValidationError(message='图形验证码错误')


#登陆表单
class SignInForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[35678]\d{9}',message='手机号码格式错误')])
    password = StringField(validators=[Length(5,30,message='密码格式错误')])
    remember = StringField()


