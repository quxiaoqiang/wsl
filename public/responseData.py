#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import redis
import sys
import platform


r = redis.StrictRedis(host='localhost', port=6379, db=0)
r2 = redis.StrictRedis(host='r-wz923deaf1b1f914.redis.rds.aliyuncs.com', port=6379, db=0)


