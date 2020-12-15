# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @File : files_manager.py

from fastapi import File, UploadFile
from typing import List
from apps.core.base_response import success
from apps.service.file_manager_service import upload


async def create_upload_file(file: UploadFile = File(...), ):
    data = await upload(file)
    return success(data=data)



# @router.get("/download/music/{music_id}", status_code=200, tags=["file manager"])
# async def download_file(music_id: str):
#     if music_id:
#         pass
#
#     filename = r"D:\Python\python3.7\Framework\FastAPI\atools\apps\resource\txt\30549edc47a75e1ca11871d20f8a66af.txt"
#
#     return FileResponse(filename, filename="1.txt")
