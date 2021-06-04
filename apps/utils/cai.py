# _*_ coding:utf-8 _*_
# @Time:2021/3/23 15:14
# @Author:Cassie·Lau
# @File cai.py

import re
import time
import random


from apscheduler.schedulers.blocking import BlockingScheduler

def format_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def total(int_list:list):
    sum_val = sum(int_list)
    parity_check = "单" if (sum_val%2) !=0 else "双"
    large_or_small = "大" if int(10)<sum_val< 19 else "小"
    return sum_val,parity_check,large_or_small

def func1():
    results = sorted([random.randint(1,6) for i in range(3)])
    a,b,c = total(results)
    print(re.sub("\[","",f"时间:{format_time()},结果为:{results},和值为:{a},奇偶性值为:{b},大小值为:{c}"))
    return results

def func2():
    scheduler = BlockingScheduler()
    scheduler.add_job(func1,'interval',seconds=5)
    scheduler.start()
func2()