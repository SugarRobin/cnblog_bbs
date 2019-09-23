from flask import Blueprint,views,render_template,request,session
from .forms import SignUpForm
from .models import FrontUser
from exts import db
from utils import xjson
from utils import safeutils
import config
from .forms import SignInForm

bp = Blueprint('front',__name__)  #因为是前台直接访问不用加url_prefix

@bp.route('/')
def index():
    return render_template('front/front_index.html')


class SignUpViews(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')

    def post(self):
        signup_form = SignUpForm(request.form)
        if signup_form.validate():

            telephone = signup_form.telephone.data
            username = signup_form.username.data
            password = signup_form.password1.data
            user = FrontUser(telephone=telephone,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return xjson.json_sucess('恭喜您，注册成功')
        else:
            return xjson.json_params_error(signup_form.get_error())



bp.add_url_rule('/signup/',view_func=SignUpViews.as_view('signup'))




class SignInViews(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        return render_template('front/front_signin.html')

    def post(self):
        signin_form = SignInForm(request.form)
        if signin_form.validate():
            telephone = signin_form.telephone.data
            password = signin_form.password.data
            remember = signin_form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.premanent = True
                return xjson.json_sucess('登陆成功')
            else:
                return xjson.json_params_error('手机号或密码错误')
        else:
            return xjson.json_params_error(signin_form.get_error())

bp.add_url_rule('/signin/',view_func=SignInViews.as_view('signin'))

