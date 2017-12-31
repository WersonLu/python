#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     刷分
   Author :       aaa
   date：          2017/12/30
-------------------------------------------------
"""
import requests
import json
import time
from Crypto.Cipher import AES
import base64

action_data = {
    "score": 500,
    "times": 100,
    "game_data": "{}"
}

session_id = "aUO9Lb/icGfHcZfLwkiv3q+8bLFeGYd373mdAKECNb8vnNYwtWSnpACb1QDO45k3NEZUhSQ+xqkoqXCoKX92plTslpwfGYC7P4EfGWLZynwqLLlihP5A9pVKR6lM6jeHd2ZM9JYGYBfZaMXfLGW0Dw\\u003d\\u003d"

aes_key = session_id[0:16]
aes_iv = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)

str_action_data = json.dumps(action_data).encode("utf-8")
print("json_str_action_data ", str_action_data)

# Pkcs7
length = 16 - (len(str_action_data) % 16)
str_action_data += bytes([length]) * length

cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data)).decode("utf-8")
print("action_data ", cipher_action_data)

post_data = {
    "base_req": {
        "session_id": session_id,
        "fast": 1,
    },
    "action_data": cipher_action_data
}

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/3/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "MicroMessenger/6.6.1.1200(0x26060130) NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"

response = requests.post(url, json=post_data, headers=headers)
print(json.loads(response.text))
