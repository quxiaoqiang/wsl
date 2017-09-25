#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from commands import *
import time
from send_mail import *

#user = 'quxiaoqiang@asean-go.com'

res = getoutput('ssh -v -p 8400 test@120.77.71.43')
if 'established' in res:
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  server started'
elif 'refused' in res:
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  server stoped'
    ret = send_mail('quxiaoqiang@asean-go.com')
    if ret:
        print 'send mail ok'
    else:
        print 'send mail failed'






