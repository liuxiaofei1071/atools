# -*- coding: utf-8 -*-
# @Time : 2020/9/24 16:59
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : tools.py


import uuid
import base64
import hashlib


class Tools:

    @staticmethod
    def uuid_name(filename):
        """uuid5 dns命名空间盐加密"""
        _uid = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        uid_name = f"{str(_uid).replace('-','')}"+"."+ filename.split('.')[1]
        return uid_name

    @staticmethod
    def uid():
        """uuid4 唯一"""
        return str(uuid.uuid4()).replace('-','')

    @staticmethod
    def sha1_salt(salt):
        """sha1 加盐加密"""
        sha1 = hashlib.sha1(salt.encode('utf-8'))
        return sha1.hexdigest()

    @staticmethod
    def base64_encode(string):
        """字符串转化base64"""
        result = base64.b64encode(string.encode('utf-8')).decode()
        return result

    @staticmethod
    def base64_decode(string):
        """base64还原字符串"""
        result = base64.b64decode(string).decode("utf-8")
        return result

    @staticmethod
    def date_format(dt):
        """datetime 格式化时间转化"""
        return f"{dt.year}-{dt.month}-{dt.day} {dt.hour}:{str(dt.minute).zfill(2)}:{str(dt.second).zfill(2)}"

    @staticmethod
    def number_0_before(number,offset:int):
        """数字补位"""
        return str(number).zfill(offset)




