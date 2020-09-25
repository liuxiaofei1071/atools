# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site :
# @File : files_manager.py

import os
import logging
from logging import handlers

LOG_LEVEL_DEBUG = logging.DEBUG
LOG_LEVEL_INFO = logging.INFO
LOG_LEVEL_WARING = logging.WARNING
LOG_LEVEL_ERROR = logging.ERROR
LOG_LEVEL_CRITICAL = logging.CRITICAL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename_path = os.path.join(BASE_DIR,"log/atools.log")

class Logger(object):

    def __init__(self, filename,fmt,level, when='D', back_count=3):
        self.filename = filename
        self.fmt = fmt
        self.level = level
        self.when = when
        self.backCount = back_count

    def generate_obj(self):
        logger = logging.getLogger(__name__)
        format_str = logging.Formatter(self.fmt)  # 设置日志格式
        logger.setLevel(self.level)  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=self.filename, when=self.when, backupCount=self.backCount,encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)  # 设置文件里写入的格式
        logger.addHandler(sh)  # 把对象加到logger里
        logger.addHandler(th)
        return logger


logger = Logger(
    filename=filename_path,
    fmt='[%(asctime)s] %(filename)s line:%(lineno)d [%(levelname)s] %(message)s',
    level=LOG_LEVEL_DEBUG,
    when='D',
    back_count=3,
).generate_obj()