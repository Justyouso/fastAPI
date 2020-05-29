# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:10

from fastapi import APIRouter


users = APIRouter()
# router.include_router(router, tags=["users"], prefix="/users")

# from app.users.views import router as users
from app.users import views