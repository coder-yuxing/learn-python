# python 正则表达式模块(re, Regular Expression)
import re

# 正则表达式前皆以 r 开头， r''
# findall: 匹配字符串中所有符合正则的内容，并返回一个list
phone_numbers = re.findall(r'\d+', '我的电话号码是：10086, 我的另一个电话号码是：10010')
print(phone_numbers)

# finditer: 匹配字符串中所有符合正则的内容，并返回一个迭代器
phone_numbers = re.finditer(r'\d+', '我的电话号码是：10086, 我的另一个电话号码是：10010')
for number in phone_numbers:
    print(number)
    print(number.group())  # 从迭代器中获取匹配到的内容

# search: 从字符串中匹配符合正则的内容，找到一个即返回
number = re.search(r'\d+', '我的电话号码是：10086, 我的另一个电话号码是：10010')
print(number)
print(number.group())  # 获取匹配的内容

# match: 从头开始匹配字符串内容，可以认为是在正则中增加了 ^ -> ^\d+
match = re.match(r'\d+', '我的电话号码是：10086, 我的另一个电话号码是：10010')
print(match)
match = re.match(r'\d+', '10086 是我的电话, 我的另一个电话号码是：10010')
print(match)
print(match.group())

# compile: 预加载正则表达式
regex = re.compile(r'\d+')
phone_numbers = regex.finditer('我的电话号码是：10086, 我的另一个电话号码是：10010')
print(phone_numbers)

number = regex.match('我的电话号码是：10086, 我的另一个电话号码是：10010')
print(number)

# 通过正则从字符串中提取内容
a_html = """
<div class='ljj' id='1'><span>林俊杰</span></div>
<div class='zjl' id='2'><span>周杰伦</span></div>
<div class='hh' id='3'><span>韩红</span></div>
<div class='tge' id='4'><span>腾格尔</span></div>
"""
regex = re.compile(r"<div class='(?P<class>.*?)' id='(?P<id>.*?)'>"
                   r"<span>(?P<name>.*?)</span></div>",
                   re.S)
context = regex.finditer(a_html)
for i in context:
    print(i.group())
    print(i.group('class'))
    print(i.group('id'))
    print(i.group('name'))
