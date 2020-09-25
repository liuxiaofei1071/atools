# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:13
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#项目资源目录
RESOURCE_PATH = os.path.join(BASE_DIR, "resource")

#部署资源目录
#PROD_RESOURCE_PATH = "/opt/resource"

TypePath = ["py", "icon", "images", "music", "video", "excel","txt"]

