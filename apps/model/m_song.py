# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 9:29 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : m_song.py

from pydantic import BaseModel
from typing import Optional


class SongItem(BaseModel):
    music_name: str
    music_path: str
    size: int
    lyrics_path: Optional[str] = None
