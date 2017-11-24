#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from commands import *
from readExcel import *
import time
from back import log


server_ip = ['test@120.77.70.65','test@120.77.70.59','test@120.77.71.43']

def ssh_server_port(server_ip):
    server_port = read_xls()
    for i in server_port:
        #ssh -v -p port username@hostip
        #telnet ip port
        #
        res = getoutput('ssh -v -p' + str(int(i[1])) +' '+ server_ip)
        if 'established' in res:
            #print time.strftime("%Y-%m-%d %H:%M:%S   ", time.localtime()) + ' ' + i[0] + ' started'
            logging.info(i[0] + '  started')
        elif 'refused' in res:
            #print time.strftime("%Y-%m-%d %H:%M:%S   ", time.localtime()) + ' ' + i[0] + ' stoped'
            logging.info(i[0] + '  stoped')

        time.sleep(5)


if __name__ == '__main__':
    server_ip = ['test@120.77.70.65', 'test@120.77.70.59', 'test@120.77.71.43']
    log.console_out('./back/access.log')

    for ip in server_ip:
        #print '-------开始检查  ' + ip + '  服务运行情况--------'
        logging.info('-------开始检查  ' + ip + '  服务运行情况--------')
        ssh_server_port(ip)

