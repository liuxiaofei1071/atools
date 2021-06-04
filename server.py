# _*_ coding:utf-8 _*_
# @Time:2020/11/2 11:34
# @Author:Cadman
# @File server.py

import uvicorn

from apps.config.secure import (
    DEBUG,
    HTTP_HOST,
    HTTP_PORT,
    HTTP_RELOAD
)
from main import create_application

app = create_application()

if __name__ == '__main__':
    uvicorn.run(
        app='server:app',
        debug=False,
        port=HTTP_PORT,
        host=HTTP_HOST,

    )
