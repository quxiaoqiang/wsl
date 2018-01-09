#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import logging, sys

'''
1.创建logger，定义输入级别
2.创建handler，用于写入日志文件
3.创建handler，用于输出到控制台
4.定义handler的输出格式
5.将logger添加到handler里面
'''
def log(message):
    # 指定日志的最低输出级别，默认为WARN级别
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # log等级的总开关
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 文件日志
    logfile = './test.log'
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)

    # 控制台日志
    console_handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)

    # 设置日志输出格式
    console_handler.formatter = formatter  # 也可以直接给formatter赋值
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 为logger添加的日志处理器
    logger.addHandler(file_handler)
    logger.info(message)

    #logger.addHandler(console_handler)
    logger.removeHandler(file_handler)
    return logger



if __name__ == '__main__':
    # 输出不同级别的log
    #log().debug('this is debug info')
    #log().info('this is information')
    #log().warn('this is warning message')
    #log().error('this is error message')
    #log().fatal('this is fatal message, it is same as logger.critical')
    #log().critical('this is critical message')
    log('ssssss')


