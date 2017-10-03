#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import logging
import datetime

log_file = "%s%s%s"%('logs/',datetime.date.today(),'.log')
logging.basicConfig(filename=log_file,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s :%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

def exit(self,user_data):
        send_str=("%s"%"301|").encode()
        self.request.send(send_str)
        self.handle()
        mes = "%s,%s"%(user_data,'logout')
        logging.info(mes)
if __name__ == '__main__':
    pass
