# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:08
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : __init__.py.py

#kafka 建立连接
"""
from kafka import KafkaConsumer
import json,time

def atest(args):
    return args["nbiot_sno"]

consumer = KafkaConsumer("rawdata",group_id='123456', bootstrap_servers=['139.196.140.161:9092'])
# consumer.subscribe(("rawdata",))
'''
for msg in consumer:
    # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    recv = json.loads(msg.value.decode('utf-8'))
    print(recv)
    print(type(recv))
'''

msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
for msg in consumer:
    # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    recv = json.loads(msg.value.decode('utf-8'))
    # print(recv)
    print("="*80)
    print(atest(recv))


"""
class Parent:
    def __init__(self,x):
        self.x = x

    def hello(self,a):
        print('我是父亲',a,self.x)


class Child(Parent):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        super(Child, self).__init__(x)

    # child类继承与 parent类
    def hello(self,b):
        # parent类中有hello方法，但是这里也定义了一个hello方法。
        # 覆盖,但是父类方法不受影响
        super(Child, self).hello(b)
        print("我是孩子",b,self.x,self.y)



        