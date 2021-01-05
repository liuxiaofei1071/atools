# _*_ coding:utf-8 _*_
# @Time:2021/1/5 11:37
# @Author:Cadman
# @File parse.py

class Parse:

    @staticmethod
    def file2name_suffix(filename):
        if "." in filename:
            # 拆分文件名称和后缀名
            start_index = filename.rindex('.')
            file_name = filename[:start_index]
            file_suffix = f".{filename[start_index + 1:]}"
        else:
            # 文件无后缀名,流文件校验
            file_suffix = ""
            file_name = filename
        return file_name,file_suffix
