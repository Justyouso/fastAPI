# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:08
import import_string
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

routers = [
    "app.users:users",
    # "app.articles:articles",
]


def register_router(app, routers):
    for r in routers:
        module = import_string(r)
        app.include_router(module, prefix="/api/" + r.split(":")[1],
                           tags=[r.split(":")[1]])


def cors(app):
    origins = ["*"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])


def create_app(config):
    app = FastAPI()
    # 跨域解决
    cors(app)
    register_router(app, routers)

    return app
