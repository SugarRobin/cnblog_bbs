from flask import Blueprint
from flask import views,render_template,request,session,redirect,url_for
from .forms import LoginForm,ResetPwdForm,RestEmailForm
from .models import CMSUser,CMSPersmission
from .decorators import login_required,permission_required
import config
from flask import g
from flask import jsonify
from exts import db
from utils import xjson

from exts import mail
from flask_mail import Message
from utils import xcache
import string,random
# from . import hook



bp = Blueprint('cms',__name__,url_prefix='/cms')

#定义一个钩子函数
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


class LoginView(views.MethodView):
    def get(self):
        return render_template('cms/cms_login.html')

    def post(self):
        login_form = LoginForm(request.form)
        if login_form.validate():
            email = login_form.email.data
            password = login_form.password.data
            remember = login_form.password.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    #如果勾选了记住我，则保存session，这样就算浏览器关闭session还是存在的
                    session.permanent = True
                return redirect(url_for('cms.index')) #因为是蓝图这里必须使用cms.index,不能使用index
            else:
                return render_template('cms/cms_login.html',message='账号或密码错误')
                #等同于 return self.get(message='账号或密码错误')
        else:
            message = login_form.errors.popitem()[1][0]
            print(message)
            # return self.get(message=message)

bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))


#注销功能
@bp.route('/logout/')
@login_required

def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

#个人主页功能
@bp.route('/profile')
@login_required
@permission_required(CMSPersmission.VISITOR) #这个装饰器要放在login_required下面，因为只有先登录了，才能进下一步验证
def profile():
    return render_template('cms/cms_profile.html')


#修改密码功能，直接使用类视图
class ResetPwdView(views.MethodView):
    decorators = [login_required] #修改密码也需要先登陆，这是类视图装饰器
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        resetpwd_form = ResetPwdForm(request.form)
        if resetpwd_form.validate():
            oldpwd = resetpwd_form.oldpwd.data
            newpwd = resetpwd_form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                #因为接受是ajax,所以这里使用jsonify返回数据
                #返回code字段表示状态码，message信息提示
                # return jsonify({"code":200,"message":"修改成功"})
                return xjson.json_sucess('修改成功')
            else:
                # return jsonify({"code":400,"message":"原密码错误"})
                return xjson.json_params_error('原密码错误')
        else:
            message = resetpwd_form.get_error()
            # return jsonify({"code":400,"message":message})
            return xjson.json_params_error(message)

bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))



#修改邮箱视图
class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetmail.html')

    def post(self):
        resetemail_form = RestEmailForm(request.form)
        if resetemail_form.validate():
            email = resetemail_form.email.data
            g.cms_user.email = email
            db.session.commit()
            return xjson.json_sucess('邮箱修改成功')
        else:
            message = resetemail_form.get_error()
            return xjson.json_params_error(message)


bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))



#测试邮件视图
@bp.route('/test_email/')
def test_email():
    msg = Message(
        'Flask项目测试邮件',  # 这是邮件主题
        sender='robin5201314love@163.com',
        recipients=['757249681@qq.com'],  # 发送给谁，这是个列表，可以有多个接收者
        body='Hello, 这是一封测试邮件，这是邮件的正文'
    )
    mail.send(msg) #发送
    return 'success'



#前端请求生成验证码视图
@bp.route('/email_captcha/')
@login_required
def email_captcha():
    #/cms/email_capthcha/?email=xxx@qq.com
    email = request.args.get('email')
    print(email)
    if not email:
        return xjson.json_params_error('请传递邮件参数！')

    #生成6位数的随机验证码
    source = list(string.ascii_letters)
    source.extend(map(lambda x:str(x),range(0,10)))
    captcha = ''.join(random.sample(source,6))

    #发送邮件
    msg = Message('BBS论坛更换邮箱验证码',
                  recipients=[email],
                  body='您的验证码：{},5分钟内邮箱'.format(captcha)
                  )
    try:
        mail.send(msg)
    except Exception as err:
        print(err)
        return xjson.json_server_error(message='邮件发送失败')


    #验证码存入memcached
    xcache.set(email,captcha)
    return xjson.json_sucess(message='邮件发送成功')


##帖子管理
@bp.route('/posts/')
@login_required
@permission_required(CMSPersmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')

#评论管理
@bp.route('/comments/')
@login_required
@permission_required(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')

#板块管理
@bp.route('/boards/')
@login_required
@permission_required(CMSPersmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')

#前台用户管理
@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')

#cms用户管理
@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


#cms用户管理
@bp.route('/croles/')
@login_required
@permission_required(CMSPersmission.ADMIN)
def croles():
    return render_template('cms/cms_roles.html')
