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
