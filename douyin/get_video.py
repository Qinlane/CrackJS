import requests
import re
from lxml import etree


def get_playaddr(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    # html = etree.HTML(res.text)
    playAddr = re.findall(r'playAddr: "(.*)",', res.text)[-1]
    playAddr = playAddr.replace('playwm', 'play')
    return playAddr



def download(video_url, file_name):
    headers = {
        'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    }
    res = requests.get(video_url, headers=headers)
    with open(file_name, 'wb') as mp4:
        for trunk in res.iter_content(1024 * 1024):
            if trunk:
                mp4.write(trunk)


if __name__ == '__main__':
    url = 'https://v.douyin.com/WoFo6A/'
    video_url = get_playaddr(url)
    download(video_url, file_name='猫精.mp4')

