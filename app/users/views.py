# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:10
from fastapi import APIRouter, Body, Depends
from app.users import schemas
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.users import crud
from typing import List
from fastapi.responses import Response
from app.utils.out_standard import success, error
# from app.routers import router
# router = APIRouter()
from app.users import users as router


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        return {"data": "", "resCode": 1, "msg": "已存在此用户"}
    return crud.create_user(db=db, user=user)


@router.get("/")
def get_user(db: Session = Depends(get_db)):
    user = crud.get_users(db=db)
    data = schemas.UserList(users=user)

    return success(data)


@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=id)
    data = schemas.User(**user.to_json())

    return success(data)
# class UserList:
#     class Item(BaseModel):
#         name: str = ""
#         age: int = 0
#
#     @router.get("/")
#     async def get_users(self: str = None):
#         return {"data": [{"name": "wc", "age": 24}]}
#
#     @router.post("/")
#     async def post_users(self: Item = Body(None, embed=False)):
#         """
#         post方法，提交json数据，formdata获取不到
#         :return:
#         """
#         return self


# class UserList1:
#     class Item(BaseModel):
#         name: str = ""
#         age: int = 0
#
#     @router.put("/")
#     async def post_users(self: Item = Body(None, embed=False)):
#         """
#         post方法，提交json数据，formdata获取不到
#         :return:
#         """
#         return self



