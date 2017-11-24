#!/usr/bin/env python
# -*- coding:utf-8 -*-


from sendMail import *
import threading
from time import *

def timeEmail():
    now = str(time.localtime()[3]) + ':' + str(time.localtime()[4])
    if now == '11:30' or now == '17:30':
        pass

timer = threading._Timer(5,timeEmail)
timer.start()


'''
def timeEmail():
    global t    #Notice: use global variable!
    t = threading.Timer(86400.0, outosend)    # 定时器
    t.start()
t = threading.Timer(5.0, outosend)
while 1:
    if time.localtime()[3] == 6:  # 判断现在是不是早晨六点
    t.start()
    break     # 线程不能重复开始，不然会有警告
'''

