

import requests

import re
from fake_useragent import UserAgent
for i in range(10,100):
    url = f"https://www.kuaidaili.com/free/inha/{i}/"


    us=UserAgent()
    header = {

        "User-Agent":us.random
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
        IP_LIST = ip + ":" + DK[IP.index(ip)] + ","
        f.write(IP_LIST)

f.close()

