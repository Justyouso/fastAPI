# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:10
from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.models.articles import Person as Article
# from app.database import
# from app.database import db1
from sqlalchemy.orm import Session

router = APIRouter()


# @router.get("/")
# def get_articles():
#     artciels = db1.query(Article).filter().first()
#     # articles = Article.query.filter().paginate(
#     #     1, per_page=10, error_out=False
#     # )
#     print("0")
#     return {}
