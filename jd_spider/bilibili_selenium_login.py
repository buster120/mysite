"""
B站的滑动验证是这样的（之前）：滑动验证码，鼠标放在图片左下角上，滑动图片才会出现，鼠标点击滑动图片，缺口才会显示
所以我们要做的是：
    1.鼠标移动到正确的元素上，显示出没有缺口的图片并下载
    2.点击元素显示出有缺口的图片并下载
    3.对比两张图片找出缺口的移动像素
    4.拖动元素

（现在这些方法已经不能用啦，B站验证方式已经换了）
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from io import BytesIO
from PIL import Image
from scrapy import Selector
import csv

browser=webdriver.Chrome(executable_path="D:/Chromedriver/chromedriver.exe")
url="https://passport.bilibili.com/login"

def compare_pixel(image1,image2,i,j):
    #判断两个像素是否相同
    pixel1=image1.load()[i,j]
    pixel2 = image2.load()[i, j]

    threshold=60 #设置阈值，因为贴图有阴影，阴影不能算，如果相差太多才能被判定找到了位置
    if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
        return True
    return False


def crop_image(image_file_name):
    #截图验证码图片
    #定位某个元素在浏览器中的位置
    time.sleep(2)
    img=browser.find_element_by_xpath("//div[@class='gt_box']") #找到图片
    location=img.location #图片位置
    print("图片的位置",location)
    size=img.size #根据做上角的位置和图片大小计算出图片右下角的位置

    top,buttom,left,right=location["y"],location["y"]+size["height"],location["x"],location["x"]+size["width"]
    print("验证码位置",left,top,right,buttom)
    screenshot=browser.get_screenshot_as_png()
    screenshot=Image.open(BytesIO(screenshot))
    captcha=screenshot.crop((int(top),int(buttom),int(left),int(right)))
    captcha.save(image_file_name)
    return captcha



def login():
    username=""
    password=""

    browser.get(url)
    browser.maximize_window() #最大化窗口，这一步非常关键！！！！。因为要截取移动像素点

    username_ele=browser.find_element_by_xpath("//input[@id='login-username']")
    password_ele = browser.find_element_by_xpath("//*[@id='login-passwd']")
    username_ele.send_keys(username)
    password_ele.send_keys(password)  #输入账号密码

    #鼠标移动到正确的元素上，显示出没有缺口的图片并下载
    slider=browser.find_element_by_xpath("//div[@class='ge_slider_knob_gt_show']")
    ActionChains(browser).move_to_element(slider).perform()

    #如何截取图片
    image1=crop_image("captcha1.png")

    #获取缺口图片
    ActionChains(browser).click_and_hold(slider).perform()
    time.sleep(1)
    image2=crop_image("captcha2.png")

    #获取缺口图片的位置
    left=60
    has_find=False
    for i in range(left,image1.size[0]): #长度：从60到最右边依次遍历
        if has_find:
            break
        for j in range(image1.size[1]):#高度：从上边到下边依次遍历
            if not compare_pixel(image1,image2,i,j):
                left=i
                has_find=True
                break
    left-=6

    #拖动图片
    #根据偏移量获取移动轨迹
    #一开始加速，然后减速，生长曲线，且加入点随机变动
    #移动轨迹，，这就不加了，有点超纲
    #ActionChains(browser).click_and_hold(slider).perform()
    ActionChains(browser).move_by_offset(xoffset=left,yoffset=0).perform() #拖动太快了，会被检测出来是机器行为
    time.sleep(0.5)
    ActionChains(browser).release().perform()
    time.sleep(3)
    try:
        browser.find_element_by_xpath("//span[contains(text(),'验证通过')]")
        return True
    except Exception as e:
        if login():
            return True






if __name__=="__main__":
    login()