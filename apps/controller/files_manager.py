# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : files_manager.py
import os
from fastapi import File, UploadFile

from apps.conf.settings import RESOURCE_PATH, TypePath
from apps.utils.content_type import ContentType
from apps.controller import router
from apps.conf import logger
from apps.utils.used.tools import Tools


@router.get("/files/", tags=["files"])
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post("/upload/",status_code=201)
async def create_upload_file(file: UploadFile = File(...)):
    response = {
        "data": {
            "is_upload": "true",
            "filename": "",
            "u_filename": "",
            "path": "",
            "size":"",
            "content_type": ""
        },
        "error": ""
    }
    logger.info(f"当前上传的文件是:{file.filename},文件类型是:{file.content_type}")
    filename, content_type,size = file.filename, file.content_type,file.spool_max_size

    try:
        _directory_name = ContentType(filename, content_type).result()
    except Exception as e:
        logger.error(e)
        _directory_name = ""

    if _directory_name in TypePath:
        _directory_name_path = os.path.join(RESOURCE_PATH, _directory_name)
        if os.path.exists(_directory_name_path):
            u_filename = f"{Tools.uuid_name(filename)}.{filename.split('.')[1]}"
            filename_full_path = os.path.join(_directory_name_path, u_filename)

            file_data = await file.read()
            with open(filename_full_path, 'wb') as f:
                f.write(file_data)
            f.close()
            response["data"]["u_filename"] = u_filename
            response["data"]["path"] = filename_full_path
            response["data"]["size"] = f"{int(size/8/1000)}k"
        else:
            response["data"]["is_upload"] = "false"
            response["error"] = f"{_directory_name_path}资源目录不存在"
            logger.error(f"{_directory_name_path}资源目录不存在")
    else:
        response["error"] = "文件类型不支持"
        response["data"]["is_upload"] = "false"

    response["data"]["filename"] = filename
    response["data"]["content_type"] = content_type
    return response
