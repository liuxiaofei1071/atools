# _*_ coding:utf-8 _*_
# @Time:2020/11/11 22:56
# @Author:Cadman
# @File file_manager_service.py

import os

from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.core.base_response import UnicornException
from apps.config.settings import TypePath, RESOURCE_PATH
from apps.utils.used.tools import Tools
from apps.utils.mysql import resource_sql, content_type_sql


async def upload(file):

    filename, content_type = file.filename, file.content_type
    print(filename,content_type)
    if "." in filename:
        # 拆分文件名称和后缀名
        start_index = filename.rindex('.')
        file_name = filename[:start_index]
        file_suffix = f".{filename[start_index + 1:]}"
    else:
        # 文件无后缀名,流文件校验
        file_suffix = ""
        file_name = filename
    # 获取文件名称
    dir_name_dict = content_type_sql.select_content_dir_record(content_type, file_suffix)
    dir_name = dir_name_dict.get("name", "")

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
        if resource_sql.check_a_file(file_name):
            resource_id = Tools.uid()
            file_data = await file.read()
            with open(filename_full_path, 'wb') as f:
                f.write(file_data)
            size = os.path.getsize(filename_full_path)
            resource_sql.create_file(resource_id, file_name, size, file_suffix, filename_full_path)

            response = {}
            response["path"] = filename_full_path
            response["filename"] = filename
            response["content_type"] = content_type
            response["size"] = size  # 文件大小bit
            return response
        else:
            code = ErrorCode.file_uploaded
            raise UnicornException(code, filename + ErrorINFO[code])
    else:
        code = ErrorCode.file_not_supported
        raise UnicornException(code, filename + ErrorINFO[code])

