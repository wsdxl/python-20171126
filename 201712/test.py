#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import os

#网址
url = "http://www.baidu.com"
#请求
request = urllib.request.Request(url)
#爬取结果
response = urllib.request.urlopen(request)
#读取结果
data = response.read()
#设置解码方式
data = data.decode('utf-8')
#获取绝对路径
path = os.path.abspath('')
dirpath = os.path.join(path, 'spider')
if os.path.isdir(dirpath):
    print('exist')
else:
    print('no exist')
    os.mkdir(dirpath)
filepath = os.path.join(dirpath, 'test1.html')
file = open(filepath, 'w', encoding='utf-8')
#写入数据
file.write(data)
