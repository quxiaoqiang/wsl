#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from login import *


url = 'http://116.10.142.251:9111/api/rest/loadometer?carrierNo=0909&lmn=A102&qts=2017-08-09+10%3A43&qte=2017-08-09+10%3A43&ts=1502246601522&version=1.0&apiKey=b1PlnYZ19sWEROUoqqnM-_U3eWVz-6Ild7b_H3yhkGY&sign=stE6HPMB4FHvbYVw5lDQFLSW5rUlc2Zr_t3E35n-P5A'

loginData('counter','Wsl123456')
doLogin()

se= session.request(method='GET', url=url, verify=False)

print se.json()