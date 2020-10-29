# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 17:13
# @Author  : wangyk
# @File    : driver_curd.py
"""
t_driver表增删改查接口
"""
import datetime
import json

import pymysql
from fastapi import *
from fastapi.responses import JSONResponse

from apps.controller import router
from apps.db.db import db


@router.get('/getInfos/', response_class=JSONResponse, tags=['select'])
async def get_infos():
    select_all = 'select * from t_drivers;'
    results = db.select(select_all)

    return {'driver_all': results}


@router.post('/creatDriver/', tags=['creat'])
async def insert_infos(driver_json: str):
    one_driver = json.loads(driver_json)
    path = one_driver.get('path')
    kind_category = one_driver.get('kind_category')
    insert_one = ''
    db.insert(insert_one)
    return
