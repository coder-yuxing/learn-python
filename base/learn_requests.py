import requests

session = requests.Session()

url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': 'username',
    'password': 'pass'
}
# 登录
session.post(url, data=data)
# print(resp.json())

my_bookshelf_api = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
# 通过session记录会话并发起下次请求
resp = session.get(my_bookshelf_api)
print(resp.json())
