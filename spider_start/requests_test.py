import requests
# res=requests.get('http://www.baidu.com')
# print(res.text)
params={
    'username':'boby',
    'passoword':'bobby'
}
res=requests.get('http://127.0.0.1:8000',params=params)


