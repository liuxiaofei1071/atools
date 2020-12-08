# -*- coding: utf-8 -*-
# @Time : 2020/10/7 9:24
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : china_city_weather_id.py

import requests
from lxml import etree

xpaths = '/html/body/div[5]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td/font/div[2]/font//text()'
url = "http://www.360doc.com/content/12/1102/09/4808208_245235392.shtml"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
html = requests.get(url, headers=headers).content.decode('utf-8')
print(html)
tree = etree.HTML(html)

hrefs = tree.xpath('//*[@id="artContent"]/font/div[2]/font/div[2]/text()')
# for i in hrefs:
#     print(i[0].text)
print(hrefs)
