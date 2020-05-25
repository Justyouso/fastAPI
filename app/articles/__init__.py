# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:10

# from fastapi import APIRouter

# from app.users.views import router as router_users

# router = APIRouter()
# router.include_router(router, tags=["users"], prefix="/users")

from app.articles.views import router as articles
