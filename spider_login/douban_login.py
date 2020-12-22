import json
import pickle #读写文件用的
import requests


def login():
    # username='17801110704'
    # password='d123456'
    url = "https://accounts.douban.com/j/mobile/login/basic"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400',
        # 'Cookie': 'bid=KOPXlytMgA8; douban-fav-remind=1; ll="108288"; apiKey=; __utmc=30149280; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1603267091; vtoken=phone_reset_password%20d23f83b3df8d4b688ce64788af80092d; _pk_id.100001.2fad=876ffc9fc02dc5c0.1603267126.1.1603267126.1603267126.; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1603267132; last_login_way=account; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19881; __utma=30149280.2123314885.1602730600.1603265673.1603269559.4; __utmz=30149280.1603269559.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __gads=ID=9c72e218527caadd:T=1602730596:S=ALNI_MZaSMN39VUNzdf-QvC9X2ohk_f1vQ; __utmb=30149280.5.10.1603269559; login_start_time=1603270617653'
    }
    post_data = {
        "ck": "",
        "name": '17801110704',
        "password": 'd12345678',
        "remember": "true",
        "ticket": ""
    }
    session = requests.session()
    response1 = session.get(url=url, headers=headers)
    response2 = session.post(url=url, headers=headers, data=post_data)
    # print(f'stuts_code = {response2.status_code}')
    # print(f'text = {response2.text}')


    # res=requests.post(url,headers=headers, data=post_data)
    res_json = json.loads(response2.text)
    if res_json['status'] == "failed":
        print("登录失败")
    else:

        print("登录成功")
    html= session.get("https://www.douban.com/").text
    if "豆友" in html:
        print("已经登录")
    else:
        print("未登录")

if __name__ == "__main__":
        login()
