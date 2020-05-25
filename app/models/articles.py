# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-22 下午4:54
from sqlalchemy import Boolean, Column, Column, ForeignKey, Integer, String, \
    Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


# class Article(db):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True)
#     title = Column(Text, doc="标题")
#     summary = Column(Text, doc="摘要")
#     body = Column(Text, doc="内容")
#     body_md = Column(Text, doc="内容markdown")
#     body_html = Column(Text, doc="内容带html")
#     timestamp = Column(DateTime, index=True,
#                        default=datetime.utcnow)
#     author_id = Column(Integer, ForeignKey('users.id'),
#                        doc="作者")
#     comments = relationship('Comment', backref='article', lazy='dynamic',
#                             doc="评论")
#     read = Column(Integer, default=0, doc="阅读量")
#
# class Comment(db):
#     __tablename__ = 'comments'
#
#     pass


class Person(Base):
    __tablename__ = "t2"
    id = Column(Integer, primary_key=True)
    person = Column(String, doc="名字")
