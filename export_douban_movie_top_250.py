# 获取豆瓣电影评分top250数据，导入csvwen文件
import csv
import re

import csvwriter as csvwriter
import requests

url = 'https://movie.douban.com/top250'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 获取页面源码
resp = requests.get(url, headers=headers)
regex = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                   r'</span>.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp;.*?'
                   r'<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                   r'</span>', re.S)
regex_finditer = regex.finditer(resp.text)
data = []
for r in regex_finditer:
    groupdict = r.groupdict()
    groupdict['year'] = groupdict['year'].strip()
    data.append(groupdict)

# 写入 csv文件
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow(d.values())
