import json
from base64 import b64encode

import requests
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_CBC

""" 网易云音乐评论信息请求参数加密过程
function a(a = 16) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",] c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c  # 获取长度为16的随机字符串
}
function b(a, b) {  # 采用AES加密算法对参数进行加密， a 为要加密的参数， b 为加密的秘钥
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) {
    var h = {}
      , i = a(16);  -> 长度为16的随机字符串
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),  -> c 函数入参中 i 为随机数，e、f均为固定常量，因此，当i固定时，可惨想c函数返回值亦为固定值
    h
}
window.asrsea = d,
... 

d(d, e, f, g) -> {
    d -> 要加密的参数
    e -> buV0x(["流泪", "强"]) -> 010001
    f -> buV0x(Rg4k.md) -> 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
    g -> buV0x(["爱心", "女孩", "惊恐", "大笑"]) -> 0CoJUm6Qyw8W8jud
}

# 执行加密函数
var bKB1x = window.asrsea(JSON.stringify(i9b), buV0x(["流泪", "强"]),
 buV0x(Rg4k.md), buV0x(["爱心", "女孩", "惊恐", "大笑"]))
e9f.data = j9a.cr0x({
                params: bKB1x.encText,
                encSecKey: bKB1x.encSecKey
            })
"""


# ase 补码
def ase_complement(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# aes 加密
def enc_aes(data: str, sec_key: str, encoding='utf-8') -> str:
    iv = "0102030405060708".encode(encoding)
    aes = AES.new(key=sec_key.encode(encoding), IV=iv, mode=MODE_CBC)
    bs = aes.encrypt(data.encode(encoding))
    return str(b64encode(bs), encoding)


def enc_params(param: str) -> str:
    first_sec_key = '0CoJUm6Qyw8W8jud'
    second_sec_key = 'Jz20MeIastSyYZ98'
    first_param = enc_aes(ase_complement(param), first_sec_key)
    return enc_aes(ase_complement(first_param), second_sec_key)


# i="Jz20MeIastSyYZ98"
def enc_sce_key() -> str:
    return 'c268fa22fe06322215535f241932ac9c9a2d8cd500f5e9ac3922a51a97232aa8' \
           '92481e696f06570e368c84aeb638468ac439237bb1a65bf86de13a4553770ef7' \
           'ff607895622255e20472fd13ed8dc5bc45a43d957ab61c52c1f4c97ce8d4f5fa' \
           '412deef5fb98cbd3787baf177262b7df3abf1989a1615ea61a6ef97f973483b4'


# 抓取网易云音乐评论信息
def get_comments() -> str:
    # 获取音乐评论的api
    get_comments_api = 'https://music.163.com/weapi/comment/resource/comments/get'
    # 实际请求参数
    real_req_params = {
        "rid": "R_SO_4_1944289962",
        "threadId": "R_SO_4_1944289962",
        "pageNo": "1",
        "pageSize": "20",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "csrf_token": ""
    }
    # 加密后的请求参数
    enc_req_param = {
        "params": enc_params(json.dumps(real_req_params)),
        "encSecKey": enc_sce_key()
    }

    # 发起请求，获取音乐评论
    resp = requests.post(get_comments_api, data=enc_req_param)
    return resp.json()


if __name__ == '__main__':
    comments = get_comments()
    print(comments)
