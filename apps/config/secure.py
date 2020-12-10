# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:11
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : secure.py
import os
import platform
from dotenv import find_dotenv, load_dotenv

#获取env文件
system_variables = "root" if platform.system() != "Linux" else os.environ["USER"]

env_name = f"{system_variables}.env"

if os.path.exists(os.path.join(os.path.dirname(__file__),env_name)):
    load_dotenv(find_dotenv(filename=env_name))
else:
    load_dotenv(find_dotenv(filename=".env"))

#[Web]
HTTP_HOST = os.getenv("HTTP_HOST")
HTTP_PORT = int(os.getenv("HTTP_PORT"))
HTTP_RELOAD = os.getenv("HTTP_RELOAD")
DEBUG = True

# 数据库配置
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DATABASE')

#secret_key 111
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))