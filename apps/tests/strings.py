# -*- coding: utf-8 -*-
# @Time : 2020/9/22 11:41
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : strings.py

# 字符串测试

a_string = "a.py"
res = a_string.count(".")
# print(res,111)
# print(all([res>1,res<1]))
# if all([res>1,res<1]):
if 1 < res < 1:
    print("格式正常")
else:
    print("格式错误")

# print(int(131.072))

#uuid 测试
import uuid

# 基于时间戳
uid1 = uuid.uuid1()
print(uid1)

# 基于md5
uid3 = uuid.uuid3(uuid.NAMESPACE_DNS, "哇-李贞贤.mp3")

# 基于随机数(16位中取)
uid4 = uuid.uuid4()
print(uid4)
print(len(str(uid4).replace("-", "")))
# 基于sha-1
uid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "a.mp3")
print(str(uid5).replace("-", ""))
print(type(uid5))


data = {"weatherinfo": {"city": "鍖椾含", "cityid": "101010100", "temp": "27.9", "WD": "鍗楅", "WS": "灏忎簬3绾�", "SD": "28%",
                        "AP": "1002hPa", "njd": "鏆傛棤瀹炲喌", "WSE": "<3", "time": "17:55", "sm": "2.1", "isRadar": "1",
                        "Radar": "JC_RADAR_AZ9010_JB"}}



import hashlib,os
def sha1_salt(salt):
    sha1 = hashlib.sha1(salt.encode('utf-8'))
    return sha1.hexdigest()
import datetime
res = str(datetime.datetime.now().date()).replace("-","")
print(res)

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


a= "1.1.1.mp3.mp4"

start = a.rindex(".")
res = a[start+1:]
res1 = a[:start]
print(res)
print(res1)


