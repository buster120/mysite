from bs4 import BeautifulSoup
import re
html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>

<body>
    <p class="div1">hello html</p>
    <input type="text" placeholder="请输入用户名">
    <div class="div1" style="">
        这是一个div
    </div>
    <p>hello html</p>
    <div class="div2" style="">
        这是一个div2
    </div>
</body>
</html>
"""
bs=BeautifulSoup(html,"html.parser")
# title_tag=bs.title
# print(title_tag.string)
# div_tag=bs.div
# print(div_tag.string)
# div_tag=bs.find('div')
# print(div_tag)
# div_tag=bs.find(id='info-955')
# div_tag=bs.find('div',id='info-955')
# div_tag=bs.find('div',id=re.compile('info-\d+'))
# div_tag=bs.find(string='scrapy分布式爬虫')
div_tag=bs.find('div',id=re.compile('info-\d+'))
# childrens=div_tag.contents #获取div_tag的目录，即子元素，但是无法获取子元素的子元素
# childrens=div_tag.descendants #可以获取div_tag下所有的子元素，逐步全部提取出来。但是会有大量的None，因为html代码中有大量的回车（为了代码格式规范）
# for child in childrens:
#     if child.name:   #将为None的子元素去掉
#         print(child.name)
# parent=bs.find('p',{'class':'name'}).parent#找到该元素的父元素
# parent=bs.find('p',{'class':'name'}).parents#找到该元素的所有祖先元素（父元素，父元素的父元素，.....）
# next_siblings=bs.find('p',{'class':'name'}).next_siblings#找到该元素之后的兄弟元素
# for siblings in next_siblings:
#     if siblings:   #将为None的子元素去掉
#         print(siblings.string)
# previous_siblings=bs.find('p',{'class':'name'}).previous_siblings#找到该元素之前的兄弟元素
# name_tag=bs.find('p',{'class':'name'})
# print(name_tag['class'])
# print(name_tag.get('class')) #两种方法一样的

from scrapy import Selector
sel=Selector(text=html)
# tag=sel.xpath('/html/body/p[1]/text()').extract()
# pass

#获取p元素
teacher_tag=sel.xpath("//div[@class='teacher_info']/p") #注：此处的class内容一定要写全，否则会报错
teacher_tag=sel.xpath("//div[@class='teacher_info info']/p")
teacher_tag=sel.xpath("//div[contains(@class='teacher_info')]/p") #加了contains后就不用写全了
teacher_tag=sel.xpath("//div[contains(@class='teacher_i')]/p")

#http://developer.mozilla.org/en-US/doce/Web/XPath/Functions  xpath的基本方法网址，打不开
