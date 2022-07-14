import requests
from lxml import etree


class Lesson(object):
    def __init__(self, title: str, src_url: str) -> None:
        self._title = title
        self._url = src_url

    def title(self) -> str:
        return self._title

    def url(self) -> str:
        return self._url


url = 'https://b.dabanjia.com/html/dbj_yy_video.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
tree = etree.HTML(resp.text)

video_div_list = tree.xpath(
        '/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div')
lessons = []
for div in video_div_list:
    li_list = div.xpath('./ul/li')
    for li in li_list:
        data_url = li.xpath('./@data-url')[0]
        url_title = li.xpath('./p/text()')[0]
        lesson = Lesson(url_title, data_url)
        lessons.append(lesson)

for les in lessons:
    l_title = les.title()
    l_url = les.url()
    if l_url == '':
        continue

    print(l_title, l_url)
    with open(f'../temp/dabanjia/{l_title}.mp4', mode='wb') as f:
        f.write(requests.get(l_url).content)

