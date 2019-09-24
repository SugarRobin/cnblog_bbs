
import os
from datetime import datetime,timedelta

'''
配置文件

'''

#session
SECRET_KEY = os.urandom(24)
#设置session的有效期为2天，若开启了session.permanet后不设置该参数，则默认为31天
PERMANENT_SESSION_LIFETIME= timedelta(days=7)

DEBUG = True

#mysql databases
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'bbs'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port = PORT,
    db = DATABASE
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


#后台session常量
CMS_USER_ID = 'HEBOANHEHE'

#前台session常量
FRONT_USER_ID = 'WFQQ132FEVFW'






#mail
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT =  '465'
MAIL_USE_SSL = True #使用SSL，端口号为465或587
MAIL_USERNAME = 'robin5201314love@163.com'
MAIL_PASSWORD = 'djkfg98ad8urjk'   #注意，这里的密码不是邮箱密码，而是授权码
MAIL_DEFAULT_SENDER = 'robin5201314love@163.com'  #默认发送者



#ueidt配置
#上传到本地
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

#上传到七牛
UEDITOR_UPLOAD_TO_QINIU = True  #如果上传到七牛这里设置为True，上传到本地则为False
UEDITOR_QINIU_ACCESS_KEY = "CccgflgUNx-CVXk8rsouzC2QGicYWCef3_jFPyJj"
UEDITOR_QINIU_SECRET_KEY = "Par6K8cPirEWGzsDP6dblBRyMkaRaL3TvtXWakXA"
UEDITOR_QINIU_BUCKET_NAME = "flaskbbs02"
UEDITOR_QINIU_DOMAIN = "http://pxwttml1j.bkt.clouddn.com"

