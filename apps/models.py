#为什么要在这个地方新建models，因为这个models是轮播图的，需要cms管理，front展示所以建在app下面

from exts import db
from datetime import datetime


class BannerModel(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    image_url = db.Column(db.String(255),nullable=False)
    link_url = db.Column(db.String(255),nullable=False)
    priority = db.Column(db.Integer,default=0)
    create_time = db.Column(db.DateTime,default=datetime.now)


