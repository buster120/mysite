import time
import requests
import re
from scrapy import Selector
import csv
import ast
import json


def parse_good():
    for n in range(100):
        com_text = requests.get(f"https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67050788310&score=0&sortType=5&page={n}&pageSize=10&isShadowSku=0&fold=1").text
        str_match = re.search('comments":(.*])',com_text)

        nodes_str=str_match.group(1)#group返回正则表达式中第一个括号内的字符，此处即为(.*])的内容
        nodes_list=json.loads(nodes_str)

        for item in nodes_list:


            conment=item["content"]
            time.sleep(0.1)
            star=item["score"]

            with open('d://JDdata9.csv', 'a', encoding="utf-8", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([star, conment])
        time.sleep(2)
            # try:
            #     next_page_ele = browser.find_element_by_xpath("//div[@id='comment']//a[@class='ui-pager-next']")
            #     next_page_ele.send_keys('\n')
            #     time.sleep(2)
            #     sel = Selector(text=browser.page_source)
            # except:
            #     has_next_page = False

if __name__ == "__main__":
    parse_good()

    # sel=Selector(text=browser.page_source)
    #
    # #good=Good(id=good_id)  #将信息放入数据库
    # name="".join(sel.xpath("//div[@class='sku-name']/text()").extract()).strip()
    # price="".join(sel.xpath(f"//span[@class='price J-p-{good_id}']/text()").extract()).strip()
    # sppj_ele=browser.find_element_by_xpath("//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")
    # sppj_ele.click()
    # time.sleep(3)
    # sel=Selector(text=browser.page_source)
    #
    #
    #
    # has_next_page=True
    # while has_next_page:
    #     all_evalutes=sel.xpath("//div[@class='comment-item']")
    #
    #     for item in all_evalutes:
    #         # good_evalute=GoodEvaluate(good=good)
    #         star=item.xpath("./div[2]/div[1]/@class").extract()[0]
    #         star=int(star[-1])
    #         conment="".join(item.xpath("./div[2]/p[1]/text()").extract()[0]).strip()
    #         # dicts={'star':star,'conment':conment}
    #         # list=[star,conment]
    #
    #         with open('d://JDdata.csv','a',encoding="utf-8", newline='') as csv_file:
    #           csv_writer = csv.writer(csv_file)
    #
    #           csv_writer.writerow([star,conment])


