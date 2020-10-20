# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 9:34 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : m_user.py

from pydantic import  BaseModel
from typing import Optional

class SecCode(BaseModel):
    cn_name:str
    username:str
    password:str
    remark:Optional[str]=None