from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from bbs import app
from exts import db
from apps.cms import models as cms_models

from apps.front import models as front_models
FrontUser = front_models.FrontUser

CMSUser = cms_models.CMSUser  #导入cmsuse类
CMSRole = cms_models.CMSRole  #导入角色类
CMSPermission = cms_models.CMSPersmission #导入权限类
from apps.models import BannerModel


manager = Manager(app)

Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.command
def create_role():
    #访问者(可以修改个人信息)
    visitor = CMSRole(name='访问者',desc='可以修改个人信息')
    visitor.permissions = CMSPermission.VISITOR

    #运营角色(修改个人信息，管理帖子，管理评论，管理前台用户)
    operator = CMSRole(name='运营',desc='管理帖子,评论,前台用户')
    operator.permissions = (
        CMSPermission.VISITOR|
        CMSPermission.POSTER |
        CMSPermission.COMMENTER |
        CMSPermission.FRONTUSER
    )

    #管理员(拥有绝大部分权限)
    admin = CMSRole(name='管理员',desc='拥有本系统的所有权限')
    admin.permissions = (
                CMSPermission.VISITOR|
                CMSPermission.POSTER |
                CMSPermission.COMMENTER |
                CMSPermission.BOARDER |
                CMSPermission.FRONTUSER |
                CMSPermission.CMSUSER
    )

    #开发者
    developer = CMSRole(name='开发者',desc='开发人员专用')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor,operator,admin,developer])
    db.session.commit()


@manager.option('-e','--email',dest='email')
@manager.option('-n','--name',dest='name')
def add_user_to_rule(email,name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户{}添加到角色{}成功'.format(email,name))
        else:
            print('没有这个角色:{}'.format(name))
    else:
        print('没有这个用户:{}'.format(email))

@manager.command
def test_permission():
    user = CMSUser.query.first() #目前我数据库只有一个账号
    if user.is_developer:
        print('用户{}有开发者的权限'.format(user.email))
    else:
        print('用户{}没有开发权限'.format(user.email))




@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('创建用户成功')


#添加前台用户
@manager.option('-t','--telephone',dest='telephone')
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')

def create_front_user(telephone,username,password):
    user = FrontUser(telephone=telephone,username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('成功创建前台用户:{}'.format(username))

if __name__ == '__main__':
    manager.run()

