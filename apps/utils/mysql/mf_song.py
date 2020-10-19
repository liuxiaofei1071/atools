# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 15:29 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : mf_song.py

# 歌曲模型
from apps.core.db import db


def insert_song(*args):
    """添加歌曲"""
    sql = f"INSERT INTO cc_song(`id`,`song_name`,`song_type`,`song_path`,`size`,`lyrics_path`,`create_time`) \
          VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}',now())"
    return db.insert(sql)


def get_one_song(song_id):
    """获取一条歌曲数据"""
    sql = f"SELECT cs.id,(SELECT `name` FROM cc_singer WHERE id=cs.singer_id) as singer, \
                   (SELECT `name` FROM cc_song_kind WHERE id=cs.song_kind_id) as song_kind,\
                   cs.song_name,cs.size \
             FROM cc_song cs WHERE id='{song_id}' AND del_status ='false'"
    result = db.get_one(sql)
    return result


def get_song_list():
    """获取所有的歌曲数据"""
    sql = f"SELECT cs.id,(SELECT `name` FROM cc_singer WHERE id=cs.singer_id) as singer,\
                         (SELECT `name` FROM cc_song_kind WHERE id=cs.song_kind_id) as song_kind,\
            cs.song_name,cs.size FROM cc_song cs WHERE cs.del_status ='false';"
    result = db.select(sql)

    return result if result else []


def check_a_song(name):
    """校验去重"""
    sql = f"select count(*) as number from cc_song where song_name='{name}'"
    result = db.get_one(sql)
    count = result.get("number")
    return True if count == 0 else False
