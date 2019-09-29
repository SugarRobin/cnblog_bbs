#为什么要在这个地方新建models，因为这个models是轮播图的，需要cms管理，front展示所以建在app下面

from exts import db
from datetime import datetime
# from .front.models import FrontUser



#轮播图表
class BannerModel(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    image_url = db.Column(db.String(255),nullable=False)
    link_url = db.Column(db.String(255),nullable=False)
    priority = db.Column(db.Integer,default=0)
    create_time = db.Column(db.DateTime,default=datetime.now)


#板块表
class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)



#帖子模型
class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    board_id = db.Column(db.Integer,db.ForeignKey('board.id'))
    author_id = db.Column(db.String(100),db.ForeignKey('front_user.id'))

    board = db.relationship("BoardModel",backref="posts")
    author = db.relationship("FrontUser",backref="posts")



#设计评论模型
class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"))
    author_id = db.Column(db.String(100),db.ForeignKey("front_user.id"),nullable=False)

    post = db.relationship("PostModel",backref='comments')
    author = db.relationship("FrontUser",backref='comments')


#帖子加精模型
class HighlightPostModel(db.Model):
    __tablename__ = 'highlight_post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"))
    create_time = db.Column(db.DateTime,default=datetime.now)

    post = db.relationship("PostModel",backref='highlight')

