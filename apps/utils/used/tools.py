# -*- coding: utf-8 -*-
# @Time : 2020/9/24 16:59
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : tools.py


import uuid
import base64
import hashlib


class Tools:

    @staticmethod
    def uuid_name(filename):
        _uid = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        uid_name = f"{str(_uid).replace('-','')}"+"."+ filename.split('.')[1]
        return uid_name

    @staticmethod
    def uid():
        uid = f"{str(uuid.uuid4()).replace('-','')}"
        return uid

    @staticmethod
    def sha1_salt(salt):
        sha1 = hashlib.sha1(salt.encode('utf-8'))
        return sha1.hexdigest()

    @staticmethod
    def base64_encode(string):
        result = base64.b64encode(string.encode('utf-8')).decode()
        return result

    @staticmethod
    def base64_decode(string):
        result = base64.b64decode(string).decode("utf-8")
        return result
