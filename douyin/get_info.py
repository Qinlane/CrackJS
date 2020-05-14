import requests
import re
from lxml import etree
from fontTools.ttLib import TTFont

headers = {
    'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
}
def get_user_info(user_url):
    res = requests.get(user_url, headers=headers)
    content = get_real_word(res.text)
    html = etree.HTML(content)
    user_name = html.xpath('//p[@class="nickname"]//text()')[-1]
    user_id = ''.join(html.xpath('//p[@class="shortid"]/i/text()')).replace(' ','')
    user_start = ''.join(html.xpath('//p[@class="follow-info"]/span[1]/span[1]//text()')).replace(' ','')
    user_fans = ''.join(html.xpath('//p[@class="follow-info"]/span[2]/span[1]//text()')).replace(' ','')
    user_praise = ''.join(html.xpath('//p[@class="follow-info"]/span[3]/span[1]//text()')).replace(' ','')
    print(user_name)
    print('抖音号:',user_id)
    print('关注:',user_start)
    print('粉丝:',user_fans)
    print('赞:',user_praise)

def get_real_word(content):
    content = content.replace('&#', '0').replace(';', '')
    # 定义字体的映射关系
    name_word_list = [
        {"name":["0xe603","0xe60d","0xe616"], "value":"0"},
        {"name":["0xe602","0xe60e","0xe618"], "value":"1"},
        {"name":["0xe605","0xe610","0xe617"], "value":"2"},
        {"name":["0xe604","0xe611","0xe61a"], "value":"3"},
        {"name":["0xe606","0xe60c","0xe619"], "value":"4"},
        {"name":["0xe607","0xe60f","0xe61b"], "value":"5"},
        {"name":["0xe608","0xe612","0xe61f"], "value":"6"},
        {"name":["0xe60a","0xe613","0xe61c"], "value":"7"},
        {"name":["0xe60b","0xe614","0xe61d"], "value":"8"},
        {"name":["0xe609","0xe615","0xe61e"], "value":"9"},
    ]

    for name_word in name_word_list:
        for font_code in name_word["name"]:
            content = re.sub(font_code, name_word["value"], content)
    return content

def batch_processing():
    '''
        user_id
        dytk
        _signature
    '''
    pass

def analysis_font():
    font = TTFont('iconfont_9eb9a50.woff')
    font.saveXML('font.xml')

def download(video_url, file_name):
    res = requests.get(video_url, headers=headers)
    with open(file_name, 'wb') as mp4:
        for trunk in res.iter_content(1024 * 1024):
            if trunk:
                mp4.write(trunk)

if __name__ == '__main__':
    # analysis_font()
    url = 'https://v.douyin.com/EEhRu9/'
    get_user_info(url)