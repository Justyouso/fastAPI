# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-25 下午8:38


def success(data, **kwargs):
    return {"data": data, "resCode": 0, "message": "", **kwargs}


def error(message, **kwargs):
    return {"data": "", "resCode": 1, "message": message, **kwargs}
