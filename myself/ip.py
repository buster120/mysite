#!/usr/bin/env python
#-*-coding=utf-8 -*-
#AUTHOR:duwentao


import requests

import re

i = input("请输入你要爬取第几页：")
url = "https://www.kuaidaili.com/free/inha/" + i +"/"

print("获取代理IP地址")

header = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
}

reponse = requests.get(url,header)
reponse.encoding='utf-8'
html = reponse.text


#p = r'<tr><td data-title="IP">(.*?)</td><td data-title="PORT">(.*?)</td><td data-title="匿名度">(.*?)</td><td data-title="类型">(.*?)</td><td data-title="位置">(.*?)</td><td data-title="响应速度">(.*?)</td><td data-title="最后验证时间">(.*?)</td></tr>'

ip = r'<td data-title="IP">(.*?)</td>'
IP = re.findall(ip,html,re.M|re.S)

dk = r'<td data-title="PORT">(.*?)</td>'
DK = re.findall(dk,html,re.M|re.S)


f=open("ip_list.txt","a")
for ip in IP:
    IP_LIST = ip + ":" + DK[IP.index(ip)] + "\n"
    f.write(IP_LIST)

f.close()

print("保存完毕")