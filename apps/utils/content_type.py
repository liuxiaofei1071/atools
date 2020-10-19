# -*- coding: utf-8 -*-
# @Time : 2020/9/21 15:03
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : content_type.py


CONTENT_TYPE = [
    {
        "type": "text/plain",
        "mappings": [
            {"suffix": ".txt", "name": "txt"}
        ]
    },{
        "type": "text/x-python",
        "mappings": [
            {"suffix": ".py", "name": "py"},
        ]
    },
    {
        "type": "image/png",
        "mappings": [
            {"suffix": ".png", "name": "images"}
        ]
    }, {
        "type": "image/jpeg",
        "mappings": [
            {"suffix": ".jpg", "name": "images"}
        ]
    }, {
        "type": "audio/mpeg",
        "mappings": [
            {"suffix": ".mp3", "name": "music"}
        ]
    }, {
        "type": "video/mp4",
        "mappings": [
            {"suffix": ".mp4", "name": "video"}
        ]
    }, {
        "type": "application/x-zip-compressed",
        "mappings": [
            {"suffix": ".zip", "name": "zip"}
        ]
    }, {
        "type": "application/vnd.ms-excel",
        "mappings": [
            {"suffix": ".xls", "name": "excel"},
            {"suffix": ".csv", "name": "excel"}
        ]
    }, {
        "type": "application/msword",
        "mappings": [
            {"suffix": ".doc", "name": "word"}
        ]
    }, {
        "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "mappings": [
            {"suffix": ".xlsx", "name": "excel"}
        ]
    }, {
        "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "mappings": [
            {"suffix": ".docx", "name": "word"}
        ]
    }
]


class ContentType:
    def __init__(self, filename, content_type):
        self.filename = filename
        self.content_type = content_type

    def result(self):
        for item in CONTENT_TYPE:
            if self.content_type == item["type"]:
                if self.filename.count(".") != 1:
                    pass
                _suffix = f".{self.filename.split('.')[1]}"
                s = (i["name"] for i in item['mappings'] if _suffix==i["suffix"] )
                return next(s)
        raise TypeError("上传的文件类型没有被支持!请检查文件类型或文件名")

