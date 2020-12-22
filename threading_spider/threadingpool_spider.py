import re
import ast
import requests
from scrapy import Selector
from urllib import parse
from datetime import datetime
from fake_useragent import UserAgent
import csv
import random
import time
from threading import Thread
from queue import Queue

list_queue = Queue()  # maxsize=10

domain = "https://bbs.csdn.net"


def get_nodes_json():
    left_menu_text = requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    nodes_str_match = re.search("forumNodes: (.*])", left_menu_text)
    if nodes_str_match:
        nodes_str = nodes_str_match.group(1).replace("null", "None")
        nodes_list = ast.literal_eval(nodes_str)
        return nodes_list
    return []


# url_list=[]
# def process_nodes_list(nodes_list):
#     for item in nodes_list:
#         if "url" in item:
#             if item["url"]:
#                 url_list.append(item["url"])
#             if "children" in item:
#                 process_nodes_list(item["children"])
all_urls = []


def get_level1_list(nodes_list):
    level1_url = []
    for item in nodes_list:
        if "url" in item and item["url"]:
            level1_url.append(item["url"])

    for url in level1_url:
        list_queue.put(parse.urljoin(domain, url))

    # return all_urls


# def get_all_urls():
#     nodes_list=get_nodes_json()
#     process_nodes_list(nodes_list)
#     level1_url=get_level1_list(nodes_list)
#     last_urls=[]
#     for url in url_list:
#         if url not in level1_url:
#             last_urls.append(url)
# all_urls=[]
# for url in last_urls:
#     all_urls.append(parse.urljoin(domain,url))
#     all_urls.append(parse.urljoin(domain,url+"/recommend"))
#     all_urls.append(parse.urljoin(domain,url+"/closed"))

# return last_urls


def get_random_ip():
    ip_list = ['114.104.143.0:9999', '36.248.132.25:9999', '123.55.101.116:9999', '47.106.162.218:80',
               '121.232.148.176:9000', '117.69.169.205:9999']
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    #     f=open('IP.txt','a+',encoding='utf-8')
    #     f.write('http://' + ip)
    #     f.write('\n')
    #     f.close()
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


class Spider_threading(Thread):
    def run(selfs):
        while 1:
            url = list_queue.get()
            print(url)
            ua = UserAgent()

            headers = {
                "user-agent": ua.random
            }
            proxies = get_random_ip()
            res_text = requests.get(url, headers=headers, proxies=proxies).text
            print(proxies)
            sel = Selector(text=res_text)
            all_trs = sel.xpath("//table[@class='forums_tab_table']//tbody//tr")
            for tr in all_trs:
                time.sleep(0.2)
                status = tr.xpath(".//td[1]/span/text()").extract()[0]
                score = tr.xpath(".//td[2]/em/text()").extract()[0]
                topic_url = parse.urljoin(domain, tr.xpath(".//td[3]/a/@href").extract()[-1])
                dd = tr.xpath(".//td[3]")
                topic_title = dd.xpath(".//a/text()").extract()[-1]
                author_url = tr.xpath(".//td[4]/a/@href").extract()[0]
                author_id = author_url.split("/")[-1]
                create_time = tr.xpath(".//td[4]/em/text()").extract()[0]
                answer_info = tr.xpath(".//td[5]/span/text()").extract()[0]
                answer_nums = answer_info.split("/")[0]
                click_nums = answer_info.split("/")[1]
                last_time_str = tr.xpath(".//td[6]/em/text()").extract()[0]
                last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M")
                with open('d://csdn.csv', 'a', encoding="utf-8", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(
                        [status, score, topic_url, topic_title, author_url, author_id, create_time, answer_info,
                         answer_nums, click_nums, last_time])
                print("哈哈哈哈哈哈哈哈哈哈或或或或或或或或或或或或或或哈哈哈哈哈哈哈哈哈")


if __name__ == "__main__":
    dd = get_nodes_json()
    get_level1_list(dd)
    # print(all_urls)
    # for url in all_urls:
    #     time.sleep(3)
    #     parse_list(url)
    ff = Spider_threading()
    ff.start()

    # parse_list("https://bbs.csdn.net/forums/Android/closed")

"""
作业：
1.将获取初试的url放到一个单独的线程中去完成
2.如何去停止线程
1.我们想手动停止 ctrl+c
    1.接收ctrl+c
    2.保存临时变量
    3.下一次启动程序的时候，我们是应该从文件中启动
2.程序有可能直接崩溃
    1.queue是内存中的，是否安全
    1.queue这种模式就不合适了，使用mysql来同步
    3.redis
3.爬虫完成以后的退出
    1.如何去判断爬虫数据已经抓取完成了


"""



