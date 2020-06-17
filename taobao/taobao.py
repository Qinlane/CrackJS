import re
import json
import requests
import time
import execjs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
}


def get_info():
    c1={
        "AntiCreep": "true",
        "api": "mtop.taobao.shop.impression.bizbanner.get",
        "data": "{'sellerId':3160935493}",
        "dataType": "json",
        "ecode": "0",
        "needLogin": "false",
        "secType": "1",
        "timeout": "3000",
        "type": "get",
        "v": "1.0"
    }

    sign = get_sign(c1, token)
    t = str(round(time.time() * 1000))
    c2 = {
        "jsv": "2.4.2",
        "appKey": "12574478",
        "t": t,
        "sign": sign,
        "api": "mtop.taobao.shop.impression.intro.get",
        "AntiCreep": "true",
        "data": "{'sellerId':%s,'shopId': %s }" % ('3160935493', '499697894'),
        "dataType": "json",
        "ecode": "0",
        "needLogin": "false",
        "secType": "1",
        "timeout": "3000",
        "type": "get",
        "v": "1.0"}

    s = requests.Session()
    res = s.post('https://acs.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/', data=c2, headers=headers)
    print(res.text)


def get_page():
    url = 'https://acs.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/'
    appKey = '12574478'
    # 获取当前时间戳
    t = str(int(time.time() * 1000))
    data = {
        "AntiCreep": "true",
        "api": "mtop.taobao.shop.impression.bizbanner.get",
        "data": "{'sellerId':3160935493}",
        "dataType": "json",
        "ecode": "0",
        "needLogin": "false",
        "secType": "1",
        "timeout": "3000",
        "type": "get",
        "v": "1.0"
    }
    params = {
        'appKey': appKey,
        'data': data
    }
    # 请求空获取cookies
    html = requests.get(url, params=params)
    # print(html.cookies)
    _m_h5_tk = html.cookies['_m_h5_tk']
    print(_m_h5_tk)
    _m_h5_tk = html.cookies['_m_h5_tk']
    _m_h5_tk_enc = html.cookies['_m_h5_tk_enc']
    token = _m_h5_tk.split('_')[0]
    cookie_t = html.cookies['t']

    sign = get_sign(data, token)
    print(sign)
    t = str(round(time.time() * 1000))
    c2 = {
        "jsv": "2.4.2",
        "appKey": "12574478",
        "t": t,
        "sign": sign,
        "api": "mtop.taobao.shop.impression.intro.get",
        "AntiCreep": "true",
        "data": "{'sellerId':%s,'shopId': %s }" % ('3160935493', '499697894'),
        "dataType": "json",
        "ecode": "0",
        "needLogin": "false",
        "secType": "1",
        "timeout": "3000",
        "type": "get",
        "v": "1.0"}

    s = requests.Session()
    res = s.post('https://h5api.m.taobao.com/h5/mtop.taobao.shop.impression.intro.get/1.0/', data=c2, headers=headers)
    print(res.text)


def get_sign(c, token):
    with open('sign.js', 'r', encoding='utf8') as f:
        ctx = execjs.compile(f.read())

    t = str(round(time.time() * 1000))
    g = "12574478"
    result = token + "&" + t + "&" + g + "&" + c['data']
    sign = ctx.call("h", result)
    return sign


if __name__ == '__main__':
    # get_info()
    get_page()


