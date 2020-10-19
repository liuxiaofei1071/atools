# -*- coding: utf-8 -*-
# @Time : 2020/9/28 14:50
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : china_weather.py


import json
import time
import requests


class Weather:
    BASE_URL = "http://www.weather.com.cn/"
    WEATHER_URL = "http://d1.weather.com.cn/weather_index/101010100.html"

    def __init__(self):
        self.headers = {
            "Referer": f"{self.BASE_URL}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        self.origin_info = {}

    def start(self):
        # result = self.__weather_info()
        #
        # send_info = self.make_msg(result) if result else None
        # print(send_info)
        # return send_info
        # print()
        if self.__weather_info():
            print(self.get_city_weather())
            print(self.get_real_time_weather())
            print(self.get_a_week_weather())
            print(self.get_weather_for_life())


    def request_info(self, url, post=False, params=None, data=None):
        if post:
            response = requests.post(url, data=json.dumps(data), headers=self.headers)
        else:
            response = requests.get(url, params=params, headers=self.headers)
        return response

    def get_city_weather(self):
        result = self.origin_info.get("cityDZ","")
        if result:
            return self.par_no_utf8_str(result)

    def get_real_time_weather(self):
        result = self.origin_info.get("dataSK", "")
        if result:
            return self.par_no_utf8_str(result)

    def get_a_week_weather(self):
        result = self.origin_info.get("fc", "")
        if result:
            return self.par_no_utf8_str(result)

    def get_weather_for_life(self):
        result = self.origin_info.get("dataZS", "")
        if result:
            return self.par_no_utf8_str(result)


    def par_no_utf8_str(self,string):
        return json.loads(string.encode('iso-8859-1').decode('utf-8'))

    def __weather_info(self):
        params = {"_": int(round(time.time() * 1000))}
        res = self.request_info(self.WEATHER_URL, params=params)
        if res.status_code == 200:
            # print(f"页面返回原始数据体: {res.text}")
            origin_info = res.text.replace("&lt;","").split(";")

            for item in origin_info:
                key,info = item.split("=")
                self.origin_info[key.split(" ")[1]] = info
            #     if "alarmDZ" in _:
            #         print(1)
            #         continue
            # # # _parse_origin_data = res.text.split("=")[1].split(";")[0]
            #     result = json.loads(info.encode('iso-8859-1').decode('utf-8'))
            #     # print(f"处理后的数据: {result}")
            # print(self.origin_info)
            return True
        return False


    def str_date(self, str_time):
        year = str_time[0:4]
        month = str_time[4:6]
        day = str_time[6:8]
        hour = str_time[8:10]
        minute = str_time[10:12]
        return f"{year}年{int(month)}月{day}日 {hour}时{minute}分"

    def weather_state(self, temp, tempn):
        temp, tempn = int(temp), int(tempn)
        current_status = -1 if temp < 15 else (0 if 15 < temp < 28 else 1)
        today_difference_temp_status = 1 if temp - tempn > 10 else 0  # 1 温差大   0 温差小
        return current_status, today_difference_temp_status

    def make_msg(self, args):
        response = {
            "msgtype": "text",
            "text": {
                "content": "",
                "mentioned_list": [],
                "mentioned_mobile_list": []
            }
        }

        city_name = args.get("weatherinfo").get("cityname")  # 地区名称
        temp = args.get("weatherinfo").get("temp").split("℃")[0]  # 温度1
        tempn = args.get("weatherinfo").get("tempn").split("℃")[0]  # 温度2
        weather = args.get("weatherinfo").get("weather")  # 天气状态
        win_direction = args.get("weatherinfo").get("wd")  # 风向
        win_level = args.get("weatherinfo").get("ws")  # 风力等级
        _weather_update_time = args.get("weatherinfo").get("fctime")  # 天气更新时间
        weather_update_time = self.str_date(_weather_update_time)
        # _temp_status, _diff_temp = self.weather_state(temp, tempn)
        # temp_status = "温度适宜" if _temp_status == 0 else ("温度较高,小心中暑" if _temp_status == 1 else "温度较低,注意保暖")
        # diff_temp = "温差较小,不用担心" if _diff_temp != 0 else "温差较大,注意加减衣服"
        msg = """各位小主,小p天气预报员为大家插播{}今日天气: {}度-{}度,风力{},\
        此刻{},全天{},数据更新时间:{},以上信息来自中国天气网,祝大家生活愉快!""".format(city_name, temp,
                                               tempn, weather,
                                               win_direction,
                                               win_level,
                                               weather_update_time)
        response["text"]["content"] = msg
        return msg

def send_msg(content):
    """发送指定信息"""
    data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": []}})
    r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)

if __name__ == '__main__':
    wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=354d0e52-8e20-44c8-8cb8-154a2ace1ecb"  # 测试机器人1号
    weather = Weather()
    result = weather.start()
    print(result,11)
    # if result:
    #     send_msg(result)