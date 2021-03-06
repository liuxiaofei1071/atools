# _*_ coding:utf-8 _*_
# @Time:2020/11/4 19:55
# @Author:Cadman
# @File model.py

import re

from typing import Optional
from pydantic import BaseModel, validator, conint


class FamilyBillUpdateModel(BaseModel):
    title: str
    money: float
    fm_type: conint(le=1, ge=0)
    payway: conint(le=6, ge=0)
    expenses_kind_id: str
    remark: Optional[str] = None
    update_by:str

class FamilyBillModel(BaseModel):
    title:str
    money:float
    fm_type: conint(le=1, ge=0)
    payway: conint(le=6, ge=0)
    expenses_kind_id:str
    remark:Optional[str] = None
    create_by:str




class AgentCode(BaseModel):
    code:str

class ScriptModel(BaseModel):
    name:str
    py_version:str
    resource_id:Optional[str] = None
    remark:Optional[str] = None
    create_by:str

class ScriptUpdateModel(BaseModel):
    name:str
    py_version : str
    remark: Optional[str] = None
    status: conint(le=1, ge=0)
    update_by:str
    resource_id:Optional[str] = None

class AnswerItem(BaseModel):
    id:str
    answer: str

class IQValidateItem(BaseModel):
    question:str
    answer:str
    kind: str
    remark:Optional[str]=None
    create_by:Optional[str]=None
    

class LoginItem(BaseModel):
    username: str
    password: str
    access_id: str


class HardwareItem(BaseModel):
    en_name: str
    cn_name: str
    parent_id: str
    remark: Optional[str] = None


"""
测试model
============================== 隔离地带-start ==================================
"""


class TokenItem(BaseModel):
    access_token: str
    token_type: str


class TestUserItem(BaseModel):
    username: str
    password: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


"""
============================== 隔离地带-end ==================================
"""


class BindService(BaseModel):
    services: list


class HostServerItem(BaseModel):
    name: str
    # ip:constr(min_length=8, max_length=14, regex=r"^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.){2}([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])$")
    ip: str
    status: conint(le=1, ge=0)
    sys_check: conint(le=2, ge=0)
    effect: conint(le=4, ge=0)
    memory: Optional[float] = None
    cpu: Optional[int] = None
    version: Optional[str] = None
    remarks: Optional[str] = None

    @validator('ip')
    def ip_re(cls, v):
        # 自定义验证 正则验证name字段 等同于上面的正则验证
        if not re.match(
                r"^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.){2}([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])$",
                v):
            # 抛出 ValueError pydantic接收到后会向外抛出 ValidationError
            raise ValueError("ip格式输入错误")
        return v


class SecCode(BaseModel):
    user_id: str
    cn_name: str
    username: str
    password: str
    remark: Optional[str] = None


class UpdateSongItem(BaseModel):
    song_name: str
    singer: Optional[str] = None


class SongItem(BaseModel):
    song_name: str
    resource_id: str
    size: int
    singer: Optional[str] = None


class ContentTypeItem(BaseModel):
    name: str
    file_type: str
    suffix: str
