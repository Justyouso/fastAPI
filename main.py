# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-21 下午5:09

import uvicorn
from config import config_module

from app import create_app

app = create_app(config_module)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=config_module.PORT)
