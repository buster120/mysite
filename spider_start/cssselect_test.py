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
from scrapy import  Selector
sel=Selector(text=html)
teacher_info_tag=sel.css('.div1::text').extract()[0]
# info_tag=sel.css('#info')
pass


#bs的接口提取方式  //不推荐使用，需要记住不同的库的方法
#xpath提取
#css提取
