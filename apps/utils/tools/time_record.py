import time

local_time = time.localtime(time.time())
s_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)  #格式化时间
print(s_time)