#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#!/uer/bin/env python
#-*- coding:utf-8 -*-

import logging

#创建日志
logger = logging.getLogger('user_login-LOG')
logger.setLevel(logging.INFO)


# create console handler and set level to debug
# 创建控制台处理程序 和设置 debug级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
# 创建文件处理程序并设置warning警告级别
fh = logging.FileHandler("access.log")
# fh.setLevel(logging.WARNING) #把WARNING级别以上的日志写到 日志文件中
fh.setLevel(logging.INFO) ##把INFO 级别以上的日志写到 日志文件中去
# fh.setLevel(logging.DEBUG)

# create formatter
# 创建格式化程序
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
# 格式化ch 和 fh
# ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
# 添加ch 和 fh 的日志记录
# logger.addHandler(ch) #显示在控制台上
logger.addHandler(fh)

# 'application' code
# 日志记录内容
# logger.debug('1、debug message') #记录debug级别的信息
logger.info('2、info message') ##记录info级别的信息
# logger.warn('3、warn message') #记录warn级别的信息
# logger.error('4、error message') #记录error级别的信息
# logger.critical('5、critical message') #记录critical级别的信息