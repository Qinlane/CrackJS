import re
import requests
import execjs


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer": "http://openlaw.cn/login.jsp",
    }

def get_password(pwd):
    with open("openlaw.js", "r", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())

    result = ctx.call("keyEncrypt", pwd)
    # print(result)
    return result

def login():
    s = requests.Session()
    res = s.get('http://openlaw.cn/login.jsp',headers=headers)
    csrf = re.findall(r'name="_csrf" value="(.*)"/>', res.text)[0]
    pwd = get_password('lola386362711')
    data = {
        '_csrf':csrf,
        'username':'qi6992295188441@163.com',
        'password':pwd,
        '_spring_security_remember_me':'true',
    }
    print(data)
    res = s.post("http://openlaw.cn/login",data=data, headers=headers,allow_redirects=False)
    print(res.status_code)
    print(s.cookies.get_dict())
    res2 = s.get("http://openlaw.cn/login.jsp?$=success",headers=headers,allow_redirects=False)
    print(res2.status_code)
    res3 = s.get("http://openlaw.cn/user/profile.jsp",headers=headers)
    print(res3.status_code)
    print(res3.text)
    



if __name__ == '__main__':
    login()

    