# -*- coding:utf-8 -*-

import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/friends/list.json" #list of follower

count = 200
cursor = -1
while True:
    params ={'count' : count, 'cursor' : cursor}
    res = twitter.get(url, params = params)

    if res.status_code == 200: #正常通信出来た場合
        friends = json.loads(res.text) #レスポンスから取得
        for names in friends['users']:
            if names['friends_count'] >= 10000 :
                print(names['name']+':'+names['screen_name']+':'+str(names['friends_count']))
    else: #正常通信出来なかった場合
        print("Failed: %d" % res.status_code)
        break

    cursor = friends['next_cursor']
    if cursor == 0:
        break
