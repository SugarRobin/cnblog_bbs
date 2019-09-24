from flask import session,redirect,url_for
from functools import wraps
import config
from flask import g

def login_required(func):
    @wraps(func) #保留func属性
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            #session中没有user_id表示没有登陆
            return redirect(url_for('cms.login'))
    return inner


def permission_required(permission):
    def outter(func):
        @wraps(func)
        def inner(*args,**kwargs):
            #判断该用户是否有权限
            if g.cms_user.has_permission(permission):
                return func(*args,**kwargs)
            else:
                #没有权限则返回首页
                return redirect(url_for('cms.index'))
        return inner
    return outter

