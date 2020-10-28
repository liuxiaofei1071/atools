# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 17:13
# @Author  : wangyk
# @File    : driver_curd.py
"""
t_driver表增删改查接口
"""
import datetime

import pymysql
from fastapi import *
from fastapi.responses import JSONResponse

from apps.controller import router
from apps.db.db import db


@router.get('/getInfos/', response_class=JSONResponse, tags=['select'])
async def get_infos():
    sql = 'select * from t_drivers;'
    cursor = db.cursor
    cursor.execute(sql)
    results = cursor.fetchall()

    return {'driver_all': results}


@router.post('/creatDriver/', tags=['creat'])
async def insert_infos(driver_json: str = Form(...)):
    return
