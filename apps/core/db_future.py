# _*_ coding:utf-8 _*_
# @Time:2020/11/23 16:25
# @Author:Cadman
# @File db_future.py

import pymysql
from DBUtils.PooledDB import PooledDB
from apps.config.settings import logger
from apps.config.secure import (
    DB_USER,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    DATABASE
)

'''
连接池
'''


class MysqlPool(object):

    def __init__(self, host, port, user, password, database):
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=3,
            # 链接池中最多共享的链接数量，
            # 0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
            # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。

            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],
            # 开始会话前执行的命令列表。
            # 如：["set datestyle to ...", "set time zone ..."]

            ping=0,
            # ping MySQL服务端，检查是否服务可用。
            # 如：0 = None = never,
            # 1 = default = whenever it is requested,
            # 2 = when a cursor is created,
            # 4 = when a query is executed,
            # 7 = always

            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset='utf8'
        )
        try:
            self.conn = self.POOL.connection()
        except Exception as e:
            print(e)
            logger.error(e)
            raise Exception(e)

    def __new__(cls, *args, **kw):
        '''
        启用单例模式
        :param args:
        :param kw:
        :return:
        '''
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect_close(self):
        '''
        关闭连接
        :return:
        '''
        self.conn.close()

    def insert(self, sql, *args):
        '''
        插入数据
        :param sql:
        :param args:字段
        :return:
        '''
        try:
            self.cursor = self.conn.cursor()
            row = self.cursor.execute(sql, args)
            self.conn.commit()
            return 1
        except Exception as e:
            logger.error(e)
            self.conn.rollback()
            return 0
        finally:
            self.cursor.close()

    def delete(self, sql, args):
        """
        删除记录
        :param sql:
        :param args: 条件
        :return:
        """
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            return 1
        except Exception as e:
            logger.exception(e)
            self.conn.rollback()
            return 0
        finally:
            self.cursor.close()

    def delete_many(self,sql,args):
        """
        删除多条记录
        :param sql:
        :param args: 条件
        :return:
        """
        self.cursor = self.conn.cursor()
        try:
            self.cursor.executemany(sql, args)
            self.conn.commit()
            return 1
        except Exception as e:
            logger.exception(e)
            self.conn.rollback()
            return 0
        finally:
            self.cursor.close()


    def update(self, sql, *args):
        """
        更新记录
        :param sql:
        :param args: 条件,可以有多个条件
        :return:
        """
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            return 1
        except Exception as e:
            self.conn.rollback()
            logger.exception(e)
            return 0
        finally:
            self.cursor.close()

    def fetch_one(self, sql, *args):
        '''
        查询单条记录
        :param sql:
        :param args:条件,可以多个条件
        :return:dict
        '''
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result if result else {}
        except Exception as e:
            logger.exception(e)
            return {}
        finally:
            self.cursor.close()

    def fetch_all(self, sql, args=None):

        '''
        批量查询记录
        :param sql:
        :param args:条件,可以为空
        :return:list
        '''
        try:
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            if args:
                self.cursor.execute(sql, args)
            else:
                self.cursor.execute(sql)
            record_list = self.cursor.fetchall()
            return record_list
        except Exception as e:
            logger.exception(e)
            return []
        finally:
            self.cursor.close()


db = MysqlPool(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DATABASE
)
