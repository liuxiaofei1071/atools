# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:13
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @File : settings.py

import os
import logging

from loguru import logger

from apps.core.logs import InterceptHandler


# [system]
# API_PREFIX = "/api"
VERSION = "1.0.1"
PROJECT_NAME = "FastAPI AToolsSystem"
DEBUG = True


# [project directory]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# [log information]
LOG_LEVEL = "INFO"
LOG_FORMAT = '{time:YYYY-MM-DD at HH:mm:ss} {level} {message}'
LOG_FILENAME = "atool.log"
LOG_PATH = os.path.join(os.path.join(BASE_DIR, "logs"),LOG_FILENAME)
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOG_LEVEL)]

logger.add(
            LOG_PATH,
            rotation="50MB",
            encoding="utf-8",
            format=LOG_FORMAT,
            level=LOG_LEVEL,
            enqueue=True,
            retention="10 days",
        )

#(开发)资源目录
RESOURCE_PATH = os.path.join(BASE_DIR, "resource")

#部署资源目录
#PROD_RESOURCE_PATH = "/opt/resource"

#系统支持文件类型
TypePath = ["py", "icon", "images", "music", "video", "excel","txt"]

#跨域
CORS_ORIGINS = ["*"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["*"]
CORS_ALLOW_HEADERS = ["*"]