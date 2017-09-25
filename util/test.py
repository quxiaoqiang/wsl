#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from public.login import *
#url = 'https://test-o.asean-go.com/platform-oss/api/oss/pretreatment/carList?companyId=100000042'
url = 'https://test-o.asean-go.com/platform-oss/api/oss/pretreatment/carList'
loginData('counter','Wsl123456')
doLogin()

se= session.request(method='GET', url=url, verify=False)

print se.text

