"""
抓取
解析
存储
"""
import re
import ast
from urllib import parse
from datetime import datetime


import requests
from scrapy import Selector

from csdn_spide.models import*

domain="https://bbs.csdn.net"
def get_nodes_json():    #通过分析可知，左侧菜单的有用信息是存在js中的
    left_menu_text= requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text #这里边提取出来的是一个js的纯文本
    nodes_str_match=re.search("forumNodes: (.*])",left_menu_text)
    if nodes_str_match:
        nodes_str=nodes_str_match.group(1).replace("null","None")#group返回正则表达式中第一个括号内的字符，此处即为(.*])的内容
        nodes_list=ast.literal_eval(nodes_str)
        return nodes_list
    return []

url_list=[]
def process_nodes_list(nodes_list):  #获取所有的url
    #将js的格式提取出url到list中
    for item in nodes_list:
        if "url" in item:
            if item["url"]:
                url_list.append(item["url"])
            if "children" in item:
                process_nodes_list(item["children"])


def get_level1_list(nodes_list):   #获取在第一层的url
    level1_url = []
    for item in nodes_list:
        if "url" in item and item["url"]:
            level1_url.append(item["url"])
    # print(len(level1_url))
    return level1_url


def get_last_urls():  #获取最终需要抓取的url
    nodes_list=get_nodes_json()
    process_nodes_list(nodes_list)
    level1_url=get_level1_list(nodes_list)
    last_urls=[]
    for url in url_list:
        if url not in level1_url:
            last_urls.append(url)
    all_urls=[]
    for url in last_urls:
        all_urls.append(parse.urljoin(domain,url)) #有的url直接以www开头，也适用parse.urljoin方法。
        all_urls.append(parse.urljoin(domain,url+"/recommend"))
        all_urls.append(parse.urljoin(domain,url+"closed"))

    return all_urls

def parse_topic(url):
    #获取帖子的详情以及回复
    pass


def parse_author(url):
    # 获取用户的详情
    pass

def parse_list(url):
    res_text=requests.get(url).text
    sel=Selector(text=res_text) #对html的文本进行实例化，这样才可以使用xpath，css语法
    all_trs=sel.xpath("//table[@class='forums_tab_table']//tr")[2:]
    for tr in all_trs:
        topic=Topic()
        if tr.xpath(".//td[1]/span/text()").extract():
            status=tr.xpath(".//td[1]/span/text()").extract()[0] #xpath是从1开始的，不是从0开始的,抽取出来是一个list，取第零个值
            topic.status=status
        if tr.xpath(".//td[2]/em/text()").extract():
            score = int(tr.xpath(".//td[2]/em/text()").extract()[0])
            topic.score = score
        if tr.xpath(".//td[3]/a/@href").extract():
            topic_url = parse.urljoin(domain,tr.xpath(".//td[3]/a/@href").extract()[0])
            topic.id = int(topic_url.split("/")[-1])
        if tr.xpath(".//td[3]/a/text()").extract():
            topic_title=tr.xpath(".//td[3]/a/text()").extract()[0]
            topic.title = topic_title
        if tr.xpath(".//td[4]/a/@href").extract():
            author_url=parse.urljoin(domain,tr.xpath(".//td[4]/a/@href").extract()[0])
            author_id=author_url.split("/")[-1]  #将url进行切割，从倒数第一个
            topic.author = author_id
        if tr.xpath(".//td[4]/em/text()").extract():
            creat_time = tr.xpath(".//td[4]/em/text()").extract()[0]
            creat_time = datetime.strptime(creat_time,"%Y-%m-%d %H:%M")
            topic.create_time = creat_time
        if tr.xpath(".//td[5]/span/text()").extract():
            answer_info = tr.xpath(".//td[5]/span/text()").extract()[0]
            answer_nums=answer_info.split("/")[0]
            click_nums = answer_info.split("/")[1]
            topic.click_nums = int(click_nums)
            topic.answer_nums = int(answer_nums)
        if tr.xpath(".//td[6]/em/text()").extract():
            last_time_str=tr.xpath(".//td[6]/em/text()").extract()[0]
            last_time=datetime.strptime(last_time_str,"%Y-%m-%d %H:%M")
            topic.last_answer_time = last_time
        # topic=Topic()


        # topic.create_time=creat_time
        # topic.last_answer_time=last_time
        # topic.score=score
        # topic.status=status
        existed_topics=Topic.select().where(Topic.id==topic.id)
        if existed_topics:
            topic.save()
        else:
            topic.save(force_insert=True)


    #     parse_topic(topic_url)
    #     parse_author(author_url)
    #
    #
    # next_page=sel.xpath("//a[@class='pageliststy next_page']/@href").extract()[0]
    # if next_page:
    #     next_url=parse.urljoin(domain,next_page[0])
    #     parse_list(next_url)






if __name__=="__main__":
    last_urls=get_last_urls()
    print(last_urls)
    print(len(last_urls))
    for url in last_urls:
        parse_list(url)


