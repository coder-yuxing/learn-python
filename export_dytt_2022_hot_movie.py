# 获取电影天堂2022必看热片
import json
import re
from typing import Any

import requests


class Movie(object):

    def __init__(self, name: str, thumnail: str, year: int, category: str,
                 director: str, download_url_list: []) -> None:
        self._name = name  # 电影名称
        self._thumbnail = thumnail  # 缩略图
        self._year = year  # 年份
        self._category = category  # 类别
        self._director = director  # 导演
        self._download_url_list = download_url_list  # 下载地址

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


class MyEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        return o.__dict__


# 电影天堂域名
domain = 'https://www.dytt89.com'
resp = requests.get(domain)
# 网页编码字符集
resp.encoding = 'gb2312'

# 从首页提取2022必看热片相关内容
regex = re.compile(r'2022必看热片.*?<ul>(?P<hot_movie_2022_msg>.*?)</ul>', re.S)
context = regex.search(resp.text)
hot_moive_2022_msg = context.group('hot_movie_2022_msg')

# 从提取内容中获取每部电影的详情页相对地址
regex = re.compile(r"<li><a href='(?P<abstract_path>.*?)'", re.S)
regex_finditer = regex.finditer(hot_moive_2022_msg)
for it in regex_finditer:
    abstract_path = it.group('abstract_path')
    # 电影的详情页地址
    movie_url = domain + abstract_path
    resp = requests.get(movie_url)
    resp.encoding = 'gb2312'
    regex = re.compile(
            r'<div id="Zoom">.*?<img.*?src="(?P<thumbnail>.*?)"'
            r'.*?◎片　　名(?P<name>.*?)<br />'
            r'.*?◎年　　代(?P<year>.*?)<br />'
            r'.*?◎类　　别(?P<category>.*?)<br />'
            r'.*?◎导　　演(?P<director>.*?)<br />'
            r'.*?<div id="downlist".*?style.*?>(?P<download_list>.*?)</div>',
            re.S)
    movie_context = regex.search(resp.text)
    thumbnail = movie_context.group('thumbnail')
    name = movie_context.group('name')
    year = movie_context.group('year').strip()
    category = movie_context.group('category')
    director = movie_context.group('director')
    regex = re.compile(r'<td.*?<a.*?>(?P<download_url>.*?</a>)', re.S)
    finditer = regex.finditer(movie_context.group('download_list'))
    download_url_list = []
    for i in finditer:
        download_url_list.append(i.group('download_url'))

    movie = Movie(name, thumbnail, int(year), category, director,
                  download_url_list)
    print(json.dumps(movie, cls=MyEncoder, indent=4))
