import requests
import execjs
import re


url = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html"

querystring  = {"noticeType":"11","areaid":"100000","noticeTitle":"","regOrg":"",} 
post_data = "draw=1&start=0&length=50"
headers = {
    # 'Cookie':'__jsluid_h=4eacfc54751178197d3e0657fb7e0125; __jsl_clearance=1587104479.367|0|SIU60aoeLS4dfB5ix%2BHzIGX%2BGdY%3D; SECTOKEN=7024650113836125923; JSESSIONID=88EB4406DBF7B9D153803C66C406F76A-n2:-1; tlb_cookie=S172.16.12.132; UM_distinctid=17186cc6c986e3-00971c16d44b7a-3a36540e-240000-17186cc6c998ac; CNZZDATA1261033118=80306127-1587099720-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1587099720',
    'Origin': "http://www.gsxt.gov.cn",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

session = requests.session()
# response = requests.post(url,data=post_data,headers=headers,params=querystring)
response = session.get(url, headers=headers)
# print(session.cookies)
# print(response.text)
# 生成cookie中的字段

res = re.findall('<script>(.*?)</script', response.text)[0]
js = res.replace('{eval(', '{var params_1 = (')
# print(js)

node = execjs.get()
ctx = node.compile(js)
js2 = ctx.eval('params_1')
# print(js2)
js3 = re.findall("document.(cookie=.+)\+';Expires", js2)[0]
# print(js3)
order_params = 'window={};' + js3
ctx1 = node.compile(order_params)
js1_params = ctx1.eval('cookie')
# print(js1_params)
cookies = js1_params.split('=')
# print(cookies)
session.cookies.set(cookies[0], cookies[1])
session.get(url, headers=headers)
print(session.cookies)
cookies = requests.utils.dict_from_cookiejar(session.cookies)

res = session.post(url, headers=headers, data=post_data, params=querystring, cookies=cookies)
if res.status_code == 200:
    res.encoding = res.apparent_encoding
    print(res.text)
