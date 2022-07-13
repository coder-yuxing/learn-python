import requests
from lxml import etree

url = 'https://www.zbj.com/search/service/?kw=sass&r=1'
resp = requests.get(url)
html_tree = etree.HTML(resp.text)
target_div_list = html_tree.xpath(
        '//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
for div in target_div_list:
    price = div.xpath('./div[3]/div[1]/span/text()')[0].strip('￥')
    title = div.xpath('./div[3]/a/text()')[0]
    company_name = div.xpath('./a/div[2]/div[1]/div/text()')[0]
    location = div.xpath('./div[3]/div[1]/div/text()')[0].strip()
