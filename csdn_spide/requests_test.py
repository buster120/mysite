import requests
from selenium import webdriver

# browser=webdriver.Chrome(executable_path="D:\python\daima")
# browser.get("https://bbs.csdn.net")
# import time
# time.sleep(5)
# cookies=browser.get_cookie()
# cookie_dict={}
# for item in cookies:
#     cookie_dict[item["name"]]=item["value"]
# print(requests.get("https://bbs.csdn.net/forums/ios",cookies=cookie_dict).text)
print(requests.get("https://bbs.csdn.net/forums/ios").text)