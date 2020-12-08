# -*- coding: utf-8 -*-
# @Time : 2020/9/25 15:47
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : music.py


from typing import Optional
from fastapi import Query

from apps.service import music_service
from apps.core.base_response import success
from apps.validator.model import SongItem, UpdateSongItem


async def create_song(song_model: SongItem):
    await music_service.create(song_model)
    return success()


async def get_song(
        song_id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    data = await music_service.get_one(song_id)
    return success(data=data)


async def get_song_list():
    data = await music_service.get_all()
    return success(data=data)


async def del_song(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    await music_service.del_one(_id)
    return success()


async def update_song(
        u_song_model: UpdateSongItem,
        _id: Optional[str] = Query(None, min_length=3, max_length=50),

):
    await music_service.update_one(u_song_model, _id)
    return success()
