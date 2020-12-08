# _*_ coding:utf-8 _*_
# @Time:2020/11/2 15:03
# @Author:Cadman
# @File logs.py

"""操作日志记录"""

import sys
import loguru
import logging
from logging import handlers

from loguru import logger
from types import FrameType
from typing import cast


class MyLogging(object):

    def __new__(cls, *args, **kwargs):
        print(args)
        filename, fmt, level = args
        logger = logging.getLogger(__name__)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        logger.setLevel(level)  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=filename,
            when="D",
            backupCount=3,
            encoding='utf-8'
        )  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)  # 设置文件里写入的格式
        logger.addHandler(sh)  # 把对象加到logger里
        logger.addHandler(th)
        return logger


class MyLogger(object):
    """无法将全局日志收集"""

    def __new__(cls, *args, **kwargs):
        logger = loguru.logger
        log_file_path, log_level, log_format = kwargs.values()
        logger.add(sys.stderr)
        logger.add(
            log_file_path,
            rotation="50MB",
            encoding="utf-8",
            format=log_format,
            level=log_level,
            enqueue=True,
            retention="10 days",
        )
        return logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:

        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # 查找发送日志消息的调用者
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage(),
        )
