# _*_ coding:utf-8 _*_
# @Time:2020/11/23 16:25
# @Author:Cassie·Lau
# @File database.py

import pymysql
from DBUtils.PooledDB import PooledDB

from apps.core.db import MySQLConfig
from apps.config.settings import logger
from apps.core.base_response import UnicornException
from apps.core.error.code_total import StatusCode
from apps.config.secure import (
    DB_USER,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    DATABASE
)

'''
DButils+pymysql
'''


class DatabaseConnectionPool(object):
    __pool = None

    def __enter__(self):
        self.conn = self.__get_conn()
        self.cursor = self.conn.cursor()
        print("数据库连接池创建con和cursor")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
        print("连接池释放conn和cursor")


    def __get_conn(self):
        if self.__pool is None:
            self.__pool = PooledDB(
                creator=pymysql,
                mincached=MySQLConfig.MIN_CACHED,
                maxcached=MySQLConfig.MAX_CACHED,
                maxshared=MySQLConfig.MAX_SHARED,
                maxconnections=MySQLConfig.MAX_CONNECTIONS,
                blocking=MySQLConfig.BLOCKING,
                maxusage=MySQLConfig.MAX_USAGE,
                setsession=MySQLConfig.SET_SESSION,
                ping=0,
                charset='utf8',
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DATABASE,
            )
        return self.__pool.connection()

    def get_conn(self,is_dict=False):
        conn = self.__get_conn()
        if is_dict:
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cursor = conn.cursor()
        return cursor,conn

class MysqlPool(object):

    def __init__(self):
        self.db = DatabaseConnectionPool()

    def __new__(cls, *args, **kw):
        '''
        启用单例模式
        :param args:
        :param kw:
        :return:
        '''
        if not hasattr(cls, '_instance'):
            cls._instance = super(MysqlPool,cls).__new__(cls,*args,**kw)
        return cls._instance

    def execute(self,sql,param=None,autoclose=False,is_dict=False):
        """
        从连接池获取连接,并根据参数类型执行对应动作
        :param sql:
        :param param:
        :param autoclose:
        :return:
        """
        cursor,conn = self.db.get_conn(is_dict=is_dict)
        count = 0
        try:
            if param:
                count = cursor.execute(sql,param)
            else:
                count = cursor.execute(sql)
            if autoclose:
                self.close(cursor,conn)

        except Exception as e:
            print(e)
        return cursor,conn,count


    # def _reConn(self, num=28800, stime=2):  # 重试连接总次数为1天,这里根据实际情况自己设置,如果服务器宕机1天都没发现就......
    #     _number = 0
    #     _status = True
    #     while _status and _number <= num:
    #         try:
    #             self.conn.ping()  # cping 校验连接是否异常
    #             _status = False
    #         except:
    #             if self.connect() == True:  # 重新连接,成功退出
    #                 _status = False
    #                 break
    #             _number += 1
    #             time.sleep(stime)  # 连接不成功,休眠3秒钟,继续循环，知道成功或重试次数结束

    def close(self,cursor,conn):
        '''
        释放连接,归还给连接池
        :return:
        '''
        cursor.close()
        conn.close()

    def insert(self, sql, *args):
        '''
        插入数据
        :param sql:
        :param args:字段
        :return:
        '''
        cursor, conn, count = self.execute(sql, args)
        try:
            conn.commit()
            self.close(cursor,conn)
        except Exception as e:
            conn.rollback()
            self.close(cursor, conn)
            logger.error(e)
            raise UnicornException(StatusCode.C10001['code'], StatusCode.C10001['msg'])


    def delete(self, sql, args):
        """
        删除记录
        :param sql:
        :param args: 条件
        :return:
        """
        cursor, conn, count = self.execute(sql, args)
        try:
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            conn.rollback()
            self.close(cursor, conn)
            logger.error(e)
            raise UnicornException(StatusCode.C10003['code'], StatusCode.C10003['msg'])


    def delete_many(self, sql, args):
        """
        删除多条记录
        :param sql:
        :param args: 条件
        :return:
        """
        cursor, conn = self.db.get_conn()
        try:
            cursor.executemany(sql, args)
            conn.commit()
            self.close(cursor, conn)
        except Exception as e:
            logger.exception(e)
            conn.rollback()
            self.close(cursor,conn)
            raise UnicornException(StatusCode.C10003['code'], StatusCode.C10003['msg'])

    def update(self, sql, *args):
        """
        更新记录
        :param sql:
        :param args: 条件,可以有多个条件
        :return:
        """
        cursor, conn, count = self.execute(sql, args)
        try:
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            conn.rollback()
            self.close(cursor, conn)
            logger.error(e)
            raise UnicornException(StatusCode.C10002['code'], StatusCode.C10002['msg'])

    def fetch_one(self, sql, *args):
        '''
        查询单条记录
        :param sql:
        :param args:条件,可以多个条件
        :return:dict
        '''
        cursor, conn, count = self.execute(sql, param=args,is_dict=True)

        try:
            result = cursor.fetchone()
            self.close(cursor, conn)
            return result if result else {}
        except Exception as e:
            self.close(cursor,conn)
            logger.error(e)
            raise UnicornException(StatusCode.C10004['code'], StatusCode.C10004['msg'])

    def fetch_all(self, sql, args=None):

        '''
        批量查询记录
        :param sql:
        :param args:条件,可以为空
        :return:list
        '''
        cursor, conn,count = self.execute(sql,param=args,is_dict=True)
        try:
            result = cursor.fetchall()
            self.close(cursor,conn)
            return result
        except Exception as e:
            logger.error(e)
            self.close(cursor,conn)
            raise UnicornException(StatusCode.C10005['code'], StatusCode.C10005['msg'])

db = MysqlPool()