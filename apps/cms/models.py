from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash  #数据库存储

class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(200),nullable=False) #这里把password字段改为_password,用户就不能直接给此字段
    #设置值了，因为用户面对的字段还是password
    email = db.Column(db.String(50),nullable=False,unique=True) #unique表示必须是唯一的
    join_time = db.Column(db.DateTime,default=datetime.now)


    #应为模型字段没有password了，但是用户还是用的password，所以必须写个__init__ 来给password赋值
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):

        self._password = generate_password_hash(raw_password)
        print('设置米啊嘛d',self._password)


    def check_password(self,raw_password): #验证密码
        result = check_password_hash(self.password,raw_password)
        return result  #返回bool值

    #######
    @property
    def permissions(self):
        #如果该用户没有任何角色，则没有权限
        if not self.roles:
            return 0
        #遍历该用户拥有的角色，获取该角色权限，并且所含有角色权限通过或运算组合在一起
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    def has_permission(self,permission):
        #把传过来的权限和该用户所拥有的权限进行与运算，得出的结果和传过来的权限比较，一致的化就拥有该权限
        # 0b00000011 & 0b00000001 ------>1 (0b00000001)
        return self.permissions & permission == permission

    @property
    def is_developer(self):
        #判断该用户是否是开发者，开发者拥有所有的权限
        return self.has_permission(CMSPersmission.ALL_PERMISSION)




#定义一个权限类
class CMSPersmission(object):
    #255的二进制表示11111111
    ALL_PERMISSION = 0b11111111   #255

    #访问者权限
    VISITOR = 0b00000001      #1

    #管理帖子权限
    POSTER = 0b00000010      #2

    #管理评论的权限
    COMMENTER = 0b00000100   #4

    #管理板块的权限
    BOARDER = 0b00001000     #8

    #管理前台用户的权限
    FRONTUSER = 0b00010000  #16

    #管理后台用户的权限
    CMSUSER = 0b00100000    #32

    #管理后台管理员的权限
    ADMIN = 0b01000000      #64



#定义角色模型并且和CMSUser模型组成多对多的关系
cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id',db.Integer,db.ForeignKey('cms_role.id'),primary_key=True),
    db.Column('cms_user_id',db.Integer,db.ForeignKey('cms_user.id'),primary_key=True)

)

#定义用户角色类
class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    desc = db.Column(db.String(200),nullable=True)
    create_time = db.Column(db.DateTime,default=datetime.now)
    permissions = db.Column(db.Integer,default=CMSPersmission.VISITOR)
    users = db.relationship('CMSUser',secondary=cms_role_user,backref='roles')


