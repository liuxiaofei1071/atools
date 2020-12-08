# _*_ coding:utf-8 _*_
# @Time:2020/11/2 16:38
# @Author:Cadman
# @File base_response.py

"""基准返回结构定义"""


def base_response(status, data=None, msg=None):
    """基础返回格式"""

    _data = {} if data is None else data
    _msg = "" if msg is None else msg

    return {
        "status": status,
        "message": _msg,
        "data": _data
    }


def success(data=None, msg=""):
    """成功返回格式"""
    return base_response(status=0, data=data, msg=msg)


def fail(status=-1, msg='', data=None):
    """失败返回格式"""
    return base_response(status, msg, data)


class UnicornException(Exception):

    def __init__(self, code, errmsg, data=None):
        """
        失败返回格式
        :param status: 状态
        :param errmsg: 错误信息
        """
        if data is None:
            data = {}
        self.code = code
        self.errmsg = errmsg
        self.data = data
