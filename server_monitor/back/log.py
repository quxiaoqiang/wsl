#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import logging

'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；日志级别大小关系为：
CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，也可以自己定义日志级别。
'''
def console_out(logFilename):
    logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',   # 定义输出log的格式
        datefmt='%Y/%m/%d %H:%M:%S',    # 日志输出时间格式
        filename=logFilename,  # log文件名
        filemode='w'    # 写入模式“w”或“a”
    )
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')#定义该handler格式
    console.setFormatter(formatter)
    # Create an instance实例
    logging.getLogger().addHandler(console)  # 实例化添加handler

if __name__ == "__main__":
    console_out('access.log')