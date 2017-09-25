#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import commands


res = commands.getoutput('telnet 127.0.0.1 80')

if 'Connected' in res:
    print 'ok'



