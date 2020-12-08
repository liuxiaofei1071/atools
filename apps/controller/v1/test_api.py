# _*_ coding:utf-8 _*_
# @Time:2020/11/13 11:09
# @Author:Cadman
# @File test_api.py

from apps.validator.model import (
    Item,
    TokenItem,
    TestUserItem
)
from datetime import datetime, timedelta
from typing import Optional, Any, Union
from starlette import status

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi import Header
from apps.config import secure


async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    print(results)
    return results


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


def check_jwt_token(
        token: Optional[str] = Header(None, alias="Authentication")
) -> Union[str, Any]:
    """
    解析验证 headers中为token的值 担任也可以用 Header(None, alias="Authentication") 或者 alias="X-token"
    :param token:
    :return:
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials token 校验失败",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            secure.SECRET_KEY,
            algorithms=[secure.ALGORITHM]
        )
        username, expire = payload.get("sub"), payload.get("exp")
        # https://www.jianshu.com/p/d4f9bc1d5aea
        print(username, expire)
        # if user is None:
        #     raise JWTError
        print(payload)
        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError) as e:
        print(e)

        print("token 校验出错了")
        raise credentials_exception


# token = create_token("liuxiaofei")
# print(token)
# check_jwt_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDczNTEzMjcsInN1YiI6ImxpdXhpYW9mZWkifQ.TQPWqsUh-TnflTuDWF-triGOJGq9NeORZhWTM1QfB_M")


async def test_user(
        token: str = Depends(check_jwt_token)
):
    return {"code": 0, "msg": "success签名通过"}
