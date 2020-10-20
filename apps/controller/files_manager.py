# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : files_manager.py
import os
from fastapi import File, UploadFile
from starlette.responses import FileResponse

from apps.conf import logger
from apps.controller import router
from apps.core.r_code import RESPONSE
from apps.utils.used.tools import Tools
from apps.utils.mysql import mf_resource
from apps.utils.content_type import ContentType
from apps.conf.settings import TypePath, RESOURCE_PATH


@router.post("/upload/", status_code=201, tags=["file manager"])
async def create_upload_file(file: UploadFile = File(...), ):
    logger.info(f"当前上传的文件是:{file.filename},文件类型是:{file.content_type}")
    filename, content_type = file.filename, file.content_type

    try:
        _directory_name = ContentType(filename, content_type).result()
    except Exception as e:
        logger.error(e)
        _directory_name = ""

    if _directory_name in TypePath:
        _directory_name_path = os.path.join(RESOURCE_PATH, _directory_name)
        if os.path.exists(_directory_name_path):
            pass
        else:
            os.chdir(RESOURCE_PATH)
            os.mkdir(_directory_name)
        u_filename = Tools.uuid_name(filename)

        filename_full_path = os.path.join(_directory_name_path, u_filename)
        resource_id = Tools.uid()
        start_index = filename.rindex(".")
        file_name = filename[:start_index]
        file_suffix = filename[start_index + 1:]

        if mf_resource.check_a_file(file_name):
            file_data = await file.read()
            with open(filename_full_path, 'wb') as f:
                f.write(file_data)
            size = os.path.getsize(filename_full_path)
            mf_resource.create_file(resource_id, file_name, size, file_suffix, filename_full_path)

            RESPONSE["data"]["path"] = filename_full_path
            RESPONSE["data"]["filename"] = filename
            RESPONSE["data"]["content_type"] = content_type
            RESPONSE["data"]["size"] = size  # 文件大小bit
        else:
            RESPONSE["error"] = "该文件已上传"
            RESPONSE["data"]["success"] = "false"

    else:
        RESPONSE["error"] = "文件类型不支持"
        RESPONSE["data"]["success"] = "false"

    return RESPONSE


@router.get("/download/music/{music_id}", status_code=200, tags=["file manager"])
async def download_file(music_id: str):
    if music_id:
        pass

    filename = r"D:\Python\python3.7\Framework\FastAPI\atools\apps\resource\txt\30549edc47a75e1ca11871d20f8a66af.txt"

    return FileResponse(filename, filename="1.txt")
