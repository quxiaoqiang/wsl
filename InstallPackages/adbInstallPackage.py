#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import commands

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
    # 获取apk_path
    apk_path = raw_input("请输入apk_path:").split(" ")
    for i in serial_numbers:
        for k in apk_path:
            if k != '':
                aa = "adb -s %s install -r %s" % (i, k)
                print aa
                bb = commands.getoutput(aa)
                print bb


if __name__ == "__main__":
    install_apks()

