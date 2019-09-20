from exts import db
import shortuuid
from werkzeug.security import generate_password_hash,check_password_hash
import enum  #导入枚举类
from datetime import datetime

class GenDerEnum(enum.Enum): #枚举
    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKNOW = 4


class FrontUser(db.Model):
    __tablename__ = 'front_user'
    #这里的id如果我们还使用自动增长，就会存在商业安全隐患,用户可以根据id推算出我们网站的人数
    #不使用自动增长，又要保证id的唯一性，我们就可以使用uuid
    #虽然UUid好用，但是它太长了，查找效率就会降低
    #这时我们就可以使用shortuuid这个库,它既满足了唯一性，又没有uuid那么长
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),unique=True)
    realname = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    gender = db.Column(db.Enum(GenDerEnum),default=GenDerEnum.UNKNOW)
    join_time = db.Column(db.DateTime,default=datetime.now)

    #对password对应的是_password，所以要做处理
    def __int__(self,*args,**kwargs):
        if 'password' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(FrontUser,self).__init__(*args,**kwargs)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,newpwd):
        self._password = generate_password_hash(newpwd)

    def chck_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)



