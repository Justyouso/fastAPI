# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:13


class BaseConfig:
    PORT = 8000


class DevelopConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Dmq@1234@119.3.230.228:3306/flask_test?charset=utf8"


config_dict = {"develop": DevelopConfig}
config_module = config_dict["develop"]
