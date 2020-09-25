# -*- coding: utf-8 -*-
# @Time : 2020/9/24 16:59
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : tools.py

import os
import uuid
import random


class Tools:

    @staticmethod
    def uuid_name(filename):
        _uid = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        uid_name = f"{str(_uid).replace('-','')}"+"."+ filename.split('.')[1]
        return uid_name