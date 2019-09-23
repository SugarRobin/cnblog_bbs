from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp,InputRequired
import hashlib


class SmsCaptchaForm(BaseForm):
    salt = 'fgeWdLwg436t@$%$^'
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}')])
    #这里的时间是毫秒，验证13位就够了，14位已经是几百年后了
    timestamp = StringField(validators=[Regexp(r'\d{13}')])

    #签名必须输入
    sign = StringField(validators=[InputRequired()])


    def validate(self):
        #首先必须通过上面的验证,否则不再继续网下执行了
        result = super(SmsCaptchaForm,self).validate()
        if not result:
            return False

        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        #md5(timestamp+telphone+salt)
        #md5函数必须要传一个bytes类型的字符串进去
        sign2 = hashlib.md5((timestamp + telephone +self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False


