import time
from selenium import webdriver
from scrapy import Selector
import csv
import random
browser=webdriver.Chrome(executable_path="D:/Chromedriver/chromedriver.exe")

def parse_good(good_id):

    browser.get(f"https://item.jd.com/{good_id}.html")
    time.sleep(2)
    sel=Selector(text=browser.page_source)

    #good=Good(id=good_id)  #将信息放入数据库
    name="".join(sel.xpath("//div[@class='sku-name']/text()").extract()).strip()
    #join的作用就是把list中的值用""中的符号连接起来，并返回一个字符串，strip的作用是把前后的空格回车等没有实际意义的字符去掉。
    price="".join(sel.xpath(f"//span[@class='price J-p-{good_id}']/text()").extract()).strip()
    sppj_ele=browser.find_element_by_xpath("//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")
    sppj_ele.click()
    time.sleep(3)
    sel=Selector(text=browser.page_source)#browser.page_source是一个固定方法，可以获取到网页运行完js之后的html（原本存在在js和html-body中的信息现在都有了）





    has_next_page=True
    while has_next_page:
        all_evalutes=sel.xpath("//div[@class='comment-item']")

        for item in all_evalutes:
            # good_evalute=GoodEvaluate(good=good)
            star=item.xpath("./div[2]/div[1]/@class").extract()[0]
            star=int(star[-1])
            conment="".join(item.xpath("./div[2]/p[1]/text()").extract()[0]).strip()
            # dicts={'star':star,'conment':conment}
            # list=[star,conment]

            with open('d://JDdata.csv','a',encoding="utf-8", newline='') as csv_file:
              csv_writer = csv.writer(csv_file)

              csv_writer.writerow([star,conment])


        try:
            next_page_ele=browser.find_element_by_xpath("//div[@id='comment']//a[@class='ui-pager-next']")
            next_page_ele.send_keys('\n')
            time.sleep(2)
            sel=Selector(text=browser.page_source)
        except:
            has_next_page=False







if __name__=="__main__":
    parse_good(61944422008)
