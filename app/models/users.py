# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-22 下午4:54
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from app.database import Base, engine
from sqlalchemy import Boolean, Column, Column, ForeignKey, Integer, String, \
    Text, DateTime


# class Article(db.Model):
#     __tablename__ = 'articles'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text, doc="标题")
#     summary = db.Column(db.Text, doc="摘要")
#     body = db.Column(db.Text, doc="内容")
#     body_md = db.Column(db.Text, doc="内容markdown")
#     body_html = db.Column(db.Text, doc="内容带html")
#     timestamp = db.Column(db.DateTime, index=True,
#                           default=datetime.utcnow)
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'),
#                           doc="作者")
#     comments = db.relationship('Comment', backref='article', lazy='dynamic',
#                                doc="评论")
#     read = db.Column(db.Integer, default=0, doc="阅读量")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def to_json(self):
        return self.__dict__


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    description = Column(String(1000), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


Base.metadata.create_all(bind=engine)
