import requests

# 百度首页
url = 'https://www.baidu.com'
# 设置header伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
}
response = requests.get(url, headers=headers)
with open('mybaidu.html', mode='w') as f:
    f.write(response.text)
response.close()

# 百度翻译
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
query = {
    'from': 'en',
    'to': 'zh',
    'query': 'dog',
    'domain': 'common',
    'transtype': 'translang',
    'sign': 871501.634748,
    'token': '64839db789f7670925a3f7d76e9b84eb'
}

headers = {
    'Cookie': 'BIDUPSID=6910438E04DE72721491B5C00388B5F6; PSTM=1613785124; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_c39fc9ce3b4dc00168d0ffef45a7aa7a1619060135529; MCITY=-131%3A; BAIDUID=E1D7110F4E1973E54A754E7EEC6EF013:SL=0:NR=10:FG=1; BDSFRCVID_BFESS=xt0OJexroG0x1aTD_F_--VemweKK1drTDYrEOwXPsp3LGJLVgzU7EG0PtEZpJqkbFfMZogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJkjoD_2fI-3H48k-4QEbbQH-UnLqbvJtgOZ04n-ah02JKjp3MOrQlRDqJj-2Rb-W20D0Pom3UTKsq76Wh35K5tTQP6rLtbEQRv4KKJxbp5AqhclMP5PbxulhUJiB5OLBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TFMj5o3DxK; APPGUIDE_10_0_2=1; H_WISE_SIDS=110085_127969_179348_180638_185633_189755_191527_194085_194520_196426_197471_197711_203518_204902_207237_207540_207697_208721_209568_210293_210323_211435_212287_212296_212416_212726_212740_212912_213030_213059_213094_213274_213357_214205_214596_214657_214790_215071_215127_215176_215461_215661_215730_215855_215893_216162_216252_216297_216332_216343_216353_216358_216450_216569_216570_216596_216634_216651_216656_216849_216927_216942_217161_217184_217227_217321_217345_217494_217753_217760_218020_218033; ZFY=DiYTviX8FiTDKTWTsKZFCQmTeGf9mBaddsV8ie5LXo4:C; BAIDUID_BFESS=E1D7110F4E1973E54A754E7EEC6EF013:SL=0:NR=10:FG=1; BA_HECTOR=a1808185240ha4ak051hc8eod14; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36544_36460_36726_36455_31660_36452_36165_36695_36697_36569_36775_36744_36760_36768_36764_26350_36685; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655631822,1655632268,1657029833,1657031383; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657031383; ab_sr=1.0.1_NDU1OGI5YTU5MjE2MTUwMzY5OGIzMWQyZGJhODA0NmY5OTVmODlhZjk3YjNiZDBkN2VmYjZjYmFmMmRlYTViMjIwZDJjNmQzZjMwNTM2Mzg5N2VjZDcwZjUyNDYzYmQxMjZjYmM3ZDliMTI0NTk5ZDllOTY2NmY0Zjc5MmM2OTc2OWY3MGI5YTU0NzBlZTVmODE0Y2I2NThmOGFkZDNmMg==',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
response = requests.post(url, query, headers=headers)
print(response.request.headers)
print(response.request.body)
print(response.json())
response.close()

# 豆瓣电影
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
response = requests.get(url, headers=headers)
print(response.json())

response.close()
