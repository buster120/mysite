import xlwt
import json
import re
import requests
import random
import time
from fake_useragent import UserAgent
#主函数
def main():
    # baseurl = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100013068434&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"

    #1.爬取网页
    proxy_list=get_ip_list()
    datalist = getData(proxy_list)                         #相当于二维数组

    #3.存储到xsl中
    savepath = "D:/linshishuju/commons.xls"
    saveData(datalist,savepath)

def get_ip_list():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "referer": "https://item.jd.com/100008341010.html"
    }
    ipurl = "http://api.89ip.cn/tqdl.html?api=1&num=60&port=&address=&isp="
    rsp = requests.get(url=ipurl, headers=head)
    rsp_text=rsp.text
    ip_list = re.findall('<br>(.*?)<br>', rsp_text)
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    return proxy_list



#0.得到一个指定URL的网页内容
ua=UserAgent()
def askUrl(url,proxies):

    head = {
        "user-agent": ua.random
    }
    print(head["user-agent"])


    response = requests.get(url=url, headers=head, proxies=proxies)


    return response

#1.爬取网页
def getData(proxy_list):
    datalist = []


    for i in range(0,10):                                   #50页的数据
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100013068434&score=0&sortType=5&page="+str(i)+"&pageSize=10&isShadowSku=0&fold=1"
        time.sleep(0.2)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}

        print(proxies)
        response = askUrl(url,proxies)                                  #调用网页函数
        html = response.text[20:-2]
        if html:
            html2 = json.loads(html)
        else:
            continue                 #用json解析json格式成为一个字典
        comments = html2["comments"]                          #找到评论标签
        for item in comments:
            data = []
            creationTime = item["creationTime"]             #评论时间
            data.append(creationTime)
            content = item["content"].replace('\n',"")      #评论详情
            data.append(content)
            datalist.append(data)
    return datalist

#3.存储在xls
def saveData(datalist,savapath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)   #创建work对象,存储文件
    sheet = book.add_sheet('dd',cell_overwrite_ok=True)         #创建工作表表单, cell 覆盖以前的内容
    col = ('评价时间','评论详情')
    for i in range(len(col)):
        sheet.write(0,i,col[i])                        #列名
    for i in range(len(datalist)):                      #行
        print('第%d条'%(i+1))
        data = datalist[i]
        for j in range(len(data)):                      #列
            sheet.write(i+1,j,data[j])
    book.save(savapath)                         #保存到xsl中
    print('save')

if __name__ == '__main__':
    main()
    print('爬取完毕')