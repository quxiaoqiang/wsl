#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import commands,sys
from testLogging.log import *

#print commands.getstatusoutput('ls ..')
#print commands.mkarg()
#print commands.mk2arg()
#print commands.warnpy3k()

def get_serial_numbers():
    devices = commands.getoutput('adb devices')  # 获取已连接的设备信息
    dev = devices.replace("\n", " ").replace("\t", " ").split(" ")  # 去掉\n和\t，并以空格分割字符串为list
    serial_numbers = []  # 取分割后生成的list中的设备serial_number保存
    for i in range(4, len(dev)):
        if dev[i] != 'device' and dev[i] != '':
            serial_numbers.append(dev[i])
    return serial_numbers

def install_apks():
    # 安装apk到已连接的设备:"adb -s serial_numbers install -r apk_path"
    serial_numbers = get_serial_numbers()
    if len(serial_numbers) ==0:
        log().warning('没有检测到已连接的设备，请重新连接设备')
        sys.exit()
    else:
        log().info('已连接的设备：%s' %serial_numbers)

    # 获取apk_path
    apk_path = raw_input("请输入apk_path:").split(" ")

    #安装apk
    for apk in apk_path:
        for num in serial_numbers:
            if apk != '':
                log().info(num)
                log().info(apk)
                comm = "adb -s %s install -r %s" %(num,apk)
                out = commands.getoutput(comm)
                log().info(out)
    return
if __name__ == "__main__":
    install_apks()

