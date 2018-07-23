# -*- coding:utf-8 -*-

import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/friends/list.json" #list of follower

count = 200
cursor = -1
while True:
    params ={'count' : count, 'cursor' : cursor}
    res = twitter.get(url, params = params)

    if res.status_code == 200: # success
        friends = json.loads(res.text)
        for names in friends['users']:
            if names['friends_count'] >= 10000 :
                print(names['name']+':'+names['screen_name']+':'+str(names['friends_count']))
    else:
        print("Failed: %d" % res.status_code)
        break

    cursor = friends['next_cursor']
    if cursor == 0:
        break
