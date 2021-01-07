# _*_ coding:utf-8 _*_
# @Time:2020/11/11 22:56
# @Author:Cadman
# @File file_manager_service.py

import os

from apps.core.db_future import db
from apps.core.error.code_total import StatusCode
from apps.core.base_response import UnicornException
from apps.config.settings import TypePath, RESOURCE_PATH
from apps.utils.used.tools import Tools
from apps.utils.parse import Parse
from apps.utils.mysql.common_sql import CommonSQL


async def upload(file):
    filename, content_type = file.filename, file.content_type
    print(filename, content_type)

    file_name,file_suffix = Parse.file2name_suffix(filename)

    # mysql connection

    # 获取文件名称
    result = db.fetch_one(CommonSQL.TYPE_NAME, content_type, file_suffix)
    dir_name = result.get("name", "")

    # 校验目录是否为系统支持资源目录
    if dir_name in TypePath:
        _directory_name_path = os.path.join(RESOURCE_PATH, dir_name)

        # 拼接资源存放目录
        if os.path.exists(_directory_name_path):
            pass
        else:
            os.chdir(RESOURCE_PATH)
            os.mkdir(dir_name)
        u_filename = Tools.uuid_name(filename)
        filename_full_path = os.path.join(_directory_name_path, u_filename)

        # 校验是否需要创建资源记录
        if db.fetch_one( CommonSQL.FILENAME_CHECK, file_name).get("number") == 0:
            resource_id = Tools.uid()
            file_data = await file.read()
            with open(filename_full_path, 'wb') as f:
                f.write(file_data)

            # 获取文件大小
            size = os.path.getsize(filename_full_path)

            db.insert(CommonSQL.RESOURCE_CREATE, resource_id, file_name, size, file_suffix, filename_full_path)

            return  {
                "id": resource_id,
                "path": filename_full_path,
                "filename": filename,
                "content_type": content_type,
                "size": size,
            }
        else:
            raise UnicornException(StatusCode.R20004["code"], filename + StatusCode.R20004["msg"])
    else:
        raise UnicornException(StatusCode.R20003["code"], filename + StatusCode.R20003["msg"])
