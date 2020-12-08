# _*_ coding:utf-8 _*_
# @Time:2020/11/12 11:01
# @Author:Cadman
# @File music_service.py

from apps.utils.used.tools import Tools
from apps.utils.mysql import music_sql
from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorINFO, ErrorCode


async def create(
        song_model
):
    song_name = song_model.song_name
    singer = song_model.singer
    size = song_model.size
    resource_id = song_model.resource_id

    song_id = Tools.uid()

    if singer:
        singer_id = Tools.uid()
        # 当歌手存在的时候,去重校验以歌曲和歌手联合唯一校验
        is_repeat = music_sql.check_song_record(song_name, singer)
        if is_repeat:
            music_sql.create_song_record(song_id, song_name, resource_id, size, singer_id=singer_id)
            music_sql.create_singer_record(singer_id, singer)
        else:
            code = ErrorCode.select_already_exists
            raise UnicornException(code, ErrorINFO[code])
    else:
        # 当歌手不存在时,去重校验只以歌曲唯一校验
        is_repeat = music_sql.check_song_record(song_name)
        if is_repeat:
            music_sql.create_song_record(song_id, song_name, resource_id, size)
        else:
            code = ErrorCode.select_already_exists
            raise UnicornException(code, ErrorINFO[code])


async def get_one(id):
    result = music_sql.select_song_record_by_id(id)
    if result:
        result["size"] = f"{round(int(result['size']) / 1024 / 1024, 2)}MB"
        return result
    else:
        code = ErrorCode.select_resource_null
        raise UnicornException(code, ErrorINFO[code])


async def get_all():
    result = music_sql.select_all_song_record()
    if result:
        for item in result:
            item["size"] = f"{round(int(item['size']) / 8 / 1024 / 1024, 2)}MB"
    return result


async def del_one(id):
    music_sql.del_one_song_record(id)


async def update_one(u_song_model, id):
    song_name = u_song_model.song_name
    singer = u_song_model.singer
    if singer:
        singer_id = music_sql.get_singer_in_song(id)
        if singer_id:
            music_sql.update_song_record(id, song_name, singer_id)
            music_sql.update_singer_record(singer, singer_id)

        else:
            singer_id = Tools.uid()
            music_sql.update_song_record(id, song_name, singer_id)
            music_sql.create_singer_record(singer_id, singer)

    else:
        music_sql.update_song_record(id, song_name)
    return
