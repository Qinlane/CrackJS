import requests
import json
import execjs

def get_content():
    url = 'http://61.191.22.196:5566/ahsxx/service/PublicBusinessHandler.ashx?name=2.1ZVNlbHRjYVJuaWFNRHB0YSph&btime=2.1MDIwMjQwNzI4MDAw&etime=2.1MDIwMjQwODIwMTAw&rainlevel=2.1OkEwMTIsLDUwNTEsMDA%3D&isoline=2.1Kk4%3D&heatRange=2.1MDU%3D&stcdtype=2.1LDEsMSwxLDEsMSow&fresh=2.1KjA%3D&points=&waterEncode=2.1cnRldQ%3D%3D&random=0.16883604640412342'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    }

    res = requests.get(url=url, headers=headers)
    res.encoding = "utf-8"
    html = json.loads(res.text)
    # data_json = html["respMsg"]
    data = html['data']
    # print(data)
    with open("sljc.js", "r", encoding="utf-8") as f:
        ctx = execjs.compile(f.read())

    fun = ctx.call("waterDecode", data)
    with open("json.txt", "w", encoding="utf-8") as f:
        f.write(fun)
    print(fun)

if __name__ == '__main__':
    get_content()
    