# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 15:29 
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @File : music_sql.py

# 歌曲模型
from apps.core.db import db


def create_song_record(song_id, song_name, resource_id, size, singer_id=None):
    """添加歌曲"""
    if singer_id:
        sql = "INSERT INTO cc_song(`id`,`song_name`,`singer_id`,`resource_id`,`size`,`create_time`) VALUES (%s,%s,%s,%s,%s,NOW())"
        return db.insert(sql, song_id, song_name, singer_id, resource_id, size)
    else:
        sql = "INSERT INTO cc_song(`id`,`song_name`,`resource_id`,`size`,`create_time`) VALUES (%s,%s,%s,%s,NOW())"
        return db.insert(sql, song_id, song_name, resource_id, size)


def create_singer_record(*args):
    sql = "INSERT INTO cc_singer(`id`,`name`,`create_time`) VALUES (%s,%s,NOW())"
    return db.insert(sql, *args)


def select_song_record_by_id(song_id):
    """获取一条歌曲数据"""
    sql = """SELECT cs.id,(SELECT `name` FROM cc_singer WHERE id=cs.singer_id) as singer, \
                   (SELECT `name` FROM cc_song_kind WHERE id=cs.song_kind_id) as song_kind,\
                   cs.song_name,cs.size \
             FROM cc_song cs WHERE `id`=%s AND del_status ='false'"""
    result = db.get_one(sql, song_id)
    return result


def select_all_song_record():
    """获取所有的歌曲数据"""
    sql = """SELECT cs.id,(SELECT `name` FROM cc_singer WHERE id=cs.singer_id) AS singer,
                         (SELECT `name` FROM cc_song_kind WHERE id=cs.song_kind_id) AS song_kind,
            cs.song_name,cs.size FROM cc_song cs WHERE cs.del_status ='false'"""
    result = db.select(sql)
    return result if result else []


def check_song_record(song_name, singer=None):
    """校验去重"""
    if singer:
        sql = "SELECT COUNT(*) AS number FROM cc_song song,cc_singer singer WHERE song.singer_id=singer.id \
               AND song.song_name= %s AND singer.name = %s"
        result = db.get_one(sql, song_name,singer)
    else:
        sql = f"SELECT COUNT(*) AS number FROM cc_song WHERE song_name=%s"
        result = db.get_one(sql, song_name)
    count = result.get("number")
    return True if count == 0 else False


def del_one_song_record(_id):
    sql = "DELETE FROM cc_song WHERE `id`=%s"
    return db.delete(sql, _id)


def update_song_record(_id, song_name, singer_id=None):
    if singer_id:
        sql = "UPDATE  cc_song SET `song_name`=%s,`singer_id`=%s, `update_time`=Now() WHERE `id`=%s"
        return db.update(sql, song_name,singer_id,_id)

    else:
        sql = "UPDATE  cc_song SET `song_name`=%s,`update_time`=NOW() WHERE `id`=%s"
        return db.update(sql, song_name,_id)


def update_singer_record(*args):
    sql = "UPDATE  cc_singer SET `name`=%s, `update_time`=NOW() WHERE `id`=%s"
    return db.update(sql, *args)


def get_singer_in_song(_id):
    sql = "SELECT `singer_id` FROM cc_song WHERE id=%s"
    info = db.get_one(sql, _id)
    singer_id = info.get("singer_id")
    return singer_id if singer_id else {}
