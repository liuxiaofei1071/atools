# _*_ coding:utf-8 _*_
# @Time:2021/1/15 11:35
# @Author:Cadman
# @File redis_db.py

import redis

from apps.config.secure import REDIS_HOST,REDIS_PORT

def redis_init()->redis.Redis:
    pool = redis.ConnectionPool(host=REDIS_HOST,port=REDIS_PORT,decode_responses=True)
    r_db = redis.Redis(connection_pool=pool)
    return r_db

r = redis_init()

