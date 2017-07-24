#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests

login_url = 'https://a.asean-go.com/common-platform/doLogin'
user_info = {'userName':'chaixinli', 'password':'Wsl123456'}
session  = requests.session()
print session
a = session.post(login_url,user_info)
print a

#result = session.get('https://o.asean-go.com/platform-oss/api/backups/getMenu')
ur = 'https://o.asean-go.com/platform-oss/api/oss/pretreatment/getDeclarations?pageNo=1&pageSize=65535&declarationStatus=2'
result = session.get(ur)
print result.content