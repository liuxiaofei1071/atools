# -*- coding: utf-8 -*-
# @Time : 2020/9/25 15:47
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : music.py


from typing import Optional
from fastapi import Query

from apps.model.m_song import SongItem
from apps.controller import router
from apps.utils.used.tools import Tools
from apps.utils.mysql import mf_song
from apps.core.r_code import RESPONSE, RESPONSE_LIST
from apps.conf import logger


@router.post("/song", tags=["song"])
async def create_song(item: SongItem):
    song_name = item.song_name
    singer = item.singer
    size = item.size
    resource_id = item.resource_id
    song_id = Tools.uid()
    if singer:
        singer_id = Tools.uid()
    # song_name, song_type = song_full_name.split(".")
    is_repeat = mf_song.check_a_song(song_name)
    if is_repeat:
        mf_song.create_a_song(song_id, song_name, singer_id, resource_id, size)
    else:
        RESPONSE["data"]["success"] = "false"
        RESPONSE["error"] = "该歌曲已存在"

    return RESPONSE


@router.get("/song", tags=["song"])
async def get_a_song(song_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    if song_id:
        result = mf_song.get_one_song(song_id)
        if result:
            result["size"] = f"{round(int(result['size']) / 1024 / 1024, 2)}MB"
            RESPONSE["data"].update(result)
        else:
            RESPONSE["data"]["success"] = "false"
            RESPONSE["error"] = "歌曲信息不存在"
    else:
        RESPONSE["data"]["success"] = "false"
        RESPONSE["error"] = "参数异常"
    return RESPONSE


@router.get("/song/list", tags=["song"])
async def song_list():
    result = mf_song.get_song_list()
    print(result)
    if result:
        for item in result:
            item["size"] = f"{round(int(item['size']) / 8 / 1024 / 1024, 2)}MB"
        RESPONSE_LIST["data"] = result
    else:
        RESPONSE_LIST["error"] = "歌曲查询数据为空"
    return RESPONSE_LIST
#     print(type(result))
#     if not result :
#         RESPONSE_LIST["error"] = "当前用户查询失败"
#     for item in result:
#         item["passwd"] = Tools.base64_decode(item["passwd"])
#     RESPONSE_LIST["data"] = result
# else:
#     RESPONSE_LIST["error"] = "用户参数不存在"
# return RESPONSE_LIST
