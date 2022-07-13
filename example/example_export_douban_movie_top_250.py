# 获取豆瓣电影评分top250数据，导入csv文件
import csv
import re

import requests


def parse_html(target_url: str) -> []:
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    # 获取页面源码
    resp = requests.get(target_url, headers=headers)
    # 获取豆瓣电影的名称、上映年份、评分
    regex = re.compile(
            r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
            r'</span>.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp;.*?'
            r'<div class="star">.*?<span class="rating_num" '
            r'property="v:average">(?P<score>.*?)'
            r'</span>', re.S)
    regex_finditer = regex.finditer(resp.text)
    result = []
    for r in regex_finditer:
        group_dict = r.groupdict()
        group_dict['year'] = group_dict['year'].strip()
        result.append(group_dict)

    return result


def save_as_csv(file_name: str, file_data: []) -> None:
    if file_name is None:
        file_name = 'data'

    with open(f'{file_name}.csv', 'w') as f:
        writer = csv.writer(f)
        for d in file_data:
            writer.writerow(d.values())


if __name__ == '__main__':
    step = 25
    data = []
    for i in range(0, 10):
        start = i * step
        url = f'https://movie.douban.com/top250?start={start}&filter='
        one_page_data = parse_html(url)
        data = data + one_page_data

    save_as_csv('dou_ban_movie_top_250', data)
