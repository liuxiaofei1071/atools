# -*- coding: utf-8 -*-
# @Time : 2020/9/22 11:41
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : strings.py

# 字符串测试

a_string = "a.py"
res = a_string.count(".")
#print(res,111)
#print(all([res>1,res<1]))
# if all([res>1,res<1]):
if 1<res<1:
    print("格式正常")
else:
    print("格式错误")

#print(int(131.072))

"""uuid 测试"""
import uuid

#基于时间戳
uid1 = uuid.uuid1()
print(uid1)

#基于md5
uid3 = uuid.uuid3(uuid.NAMESPACE_DNS,"哇-李贞贤.mp3")

#基于随机数(16位中取)
uid4 = uuid.uuid4()
print(uid4)
print(len(str(uid4).replace("-","")))
#基于sha-1
uid5 = uuid.uuid5(uuid.NAMESPACE_DNS,"a.mp3")
print(str(uid5).replace("-",""))
print(type(uid5))

