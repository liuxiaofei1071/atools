# _*_ coding:utf-8 _*_
# @Time:2020/11/12 11:01
# @Author:Cadman
# @File user_service.py

from datetime import datetime, timedelta
from typing import Optional, Any, Union
from starlette import status
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi import Header
from apps.config import secure
from apps.core.db.redis_db import r

from apps.utils.rsa import OperateRSA
from apps.utils.used.tools import Tools
from apps.utils.mysql import user_sql
from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.core.base_response import UnicornException


async def sec_list(_id):
    result = user_sql.get_user_code_list(_id)
    if result:
        for item in result:
            item["passwd"] = Tools.base64_decode(item["passwd"])
    return result


async def create(sec_model):
    user_id = sec_model.user_id
    cn_name = sec_model.cn_name
    username = sec_model.username
    password = Tools.base64_encode(sec_model.password)
    remark = sec_model.remark
    id = Tools.uid()
    login_name = user_sql.get_user_name(user_id)
    if login_name:
        if user_sql.check_sec_record(cn_name):
            salt = Tools.sha1_salt(login_name)
            user_sql.create_sec_code(id, user_id, cn_name, username, password, salt, salt, remark)
        else:
            code = ErrorCode.select_already_exists
            raise UnicornException(code, ErrorINFO[code])
    else:
        code = ErrorCode.not_user
        raise UnicornException(code, ErrorINFO[code])


async def login_service(login_model):
    _username = login_model.username
    _password = login_model.password
    access_id = login_model.access_id

    # rsa校验
    private_key = r.hget(name=access_id,key="public_key")
    if private_key:
        orsa = OperateRSA()
        reduction_username = orsa.private_b64(_username, private_key)
        reduction_password = orsa.private_b64(_password, private_key)
        # print(f"rsa解析账号：{reduction_username}")
        # print(f"rsa解析密码：{reduction_password}")
        if reduction_username and reduction_password:
            r.delete(access_id)
            user_dict = user_sql.check_auth_record(reduction_username)
            if user_dict:
                username = user_dict.get("identifier")
                password = user_dict.get("password")
                # print(f"数据库存储账号：{username}")
                # print(f"数据库存储密码：{password}")
                if all({reduction_username == username, reduction_password == password}):
                    u_dict = user_sql.get_user_record(username)
                    if u_dict:
                        uid,nickname = u_dict.get('id'),u_dict.get('nick_name')
                        access_token = create_token(uid)
                        return {"token":access_token,"nickname":nickname,"user_id":uid}
                    else:
                        code = ErrorCode.user_unknown_exception
                else:
                    code = ErrorCode.user_passwd_error
            else:
                code = ErrorCode.not_user
        else:
            code = ErrorCode.secret_error
    else:
        code = ErrorCode.access_error

    raise UnicornException(code, ErrorINFO[code])


def create_token(
        subject: Union[str, Any],
        expires_delda: timedelta = None
) -> str:
    """

    :param subject: token值
    :param expires_delda: 过期时间
    :return:
    """
    if expires_delda:
        expire = datetime.utcnow() + expires_delda
    else:
        expire = datetime.utcnow() + timedelta(minutes=secure.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, secure.SECRET_KEY, algorithm=secure.ALGORITHM)
    return encode_jwt


async def generate_rsa():
    id = Tools.uid()
    public_key, private_key = OperateRSA().generate_rsa
    # user_sql.create_rsa_record(id, private_key)
    r.hset(id,"public_key",private_key)

    return {
        "access_id": id,
        "public_key": public_key
    }



