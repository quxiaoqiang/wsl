#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os, time, hashlib

#os.system('py.test ./test.py --html=ceshi.html')
#time.sleep(1)
#os.system('open ceshi.html')

API_Key = 'b1PlnYZ19sWEROUoqqnM-_U3eWVz-6Ild7b_H3yhkGY'
Security_Key = '85MK-zLGmtFTbS2NTTntMINox2mk69ujX-pWl0zH6Zc'

dit = {
    'apiKey':'b1PlnYZ19sWEROUoqqnM-_U3eWVz-6Ild7b_H3yhkGY',
    'carrierNo':'JIN9999',
    'lmn':'A102',
    'qte': '2017-08-10+16:56',
    'qts':'2017-08-10+16:56',
    'ts':'1502765233',
    'version':'1.0',
}

sss = "apiKey=b1PlnYZ19sWEROUoqqnM-_U3eWVz-6Ild7b_H3yhkGY+carrierNo=JIN9999+lmn=A102+qte=2017-08-10+16:56+qts=2017-08-10+16:56+ts=1502765233+version=1.0"

ss = hashlib.sha256(bytes('85MK-zLGmtFTbS2NTTntMINox2mk69ujX-pWl0zH6Zc'))
ss.update(sss)



print ss.hexdigest()


#7a4621a731eeebb71268893339aa7267452fed69ba11934e5b077a3447042e98
#thCv2_IV1DULlpFeLa_Dh9mJOPO_t9zajIq3dVqpmqA

