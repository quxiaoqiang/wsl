#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from commands import *
from readExcel import *
import time

server_ip = ['test@120.77.70.65','test@120.77.70.59','test@120.77.71.43']

def ssh_server_port(server_ip):
    server_port = read_xls()
    for i in server_port:

        res = getoutput('ssh -v -p' + str(int(i[1])) +' '+ server_ip[0])
        if 'established' in res:
            print time.strftime("%Y-%m-%d %H:%M:%S   ", time.localtime()) + ' ' + i[0] + ' started'
        elif 'refused' in res:
            print time.strftime("%Y-%m-%d %H:%M:%S   ", time.localtime()) + ' ' + i[0] + ' stoped'
        time.sleep(5)



if __name__ == '__main__':
    ssh_server_port(server_ip)