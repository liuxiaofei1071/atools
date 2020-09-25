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
from apps.controller import router
from fastapi.responses import JSONResponse


# mysql 连接
def mysql_client():
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='driver_manager',
        charset='utf8'
    )
    return db


@router.get('/getInfos/', response_class=JSONResponse, tags=['select'])
async def get_infos():
    db = mysql_client()
    sql = 'select * from t_drivers;'
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    driver_infos = []

    for result in results:
        one_data = list(result)
        temp = []
        for i in one_data:
            if isinstance(i, datetime.datetime):
                i = i.strftime("%Y-%m-%d %H:%M:%S")
                temp.append(i)
            else:
                temp.append(i)
        driver_infos.append(dict(zip([key[0] for key in cursor.description], temp)))

    return {'driver_all': driver_infos}


@router.post('/creatDriver/', tags=['creat'])
async def insert_infos(driver_json: str = Form(...)):
    return
