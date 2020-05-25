# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-25 下午2:57

from sqlalchemy.orm import Session
from app.models import users
from app.users import schemas
from app.database import get_db
from fastapi import Depends


def get_user(db: Session, user_id: int):
    return db.query(users.User).filter(users.User.id == user_id).first()


def get_user_by_email(db: Session, email: str=None):
    return db.query(users.User).filter(users.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    query_set = db.query(users.User)
    return query_set.offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate = None):
    fake_hashed_password = user.password + "wangchao"
    db_user = users.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = users.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
