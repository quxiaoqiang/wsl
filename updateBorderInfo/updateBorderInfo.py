#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import pymysql
from readExcel import readExcel

config_prod = {
    'host' : 'rm-wz9g1fs1leq7ou582.mysql.rds.aliyuncs.com',
    'port' : 3306,
    'user' : 'oss_rw',
    'password' : 't$6&s2*Ynwq6iCr',
    'db' : 'rainbow_oss'}

config_test = {
    'host' : 'rm-wz90mmmp086g535z1o.mysql.rds.aliyuncs.com',
    'port' : 3306,
    'user' : 'oss_rw',
    'password' : '0ss#pAss#21',
    'db' : 'rainbow_oss'}

def borderInfo():
    list= []
    borderList = readExcel()
    for i in borderList:
        a = i[13:15]
        a.append(i[7])
        list.append(a)
    return list

def updateBorderInfo():
    conn = pymysql.connect(**config_test)
    cur = conn.cursor()
    for i in borderInfo():
        sql = "update t_border set border_bank=" + "'" + i[1] + "'" + "," + "border_phone=" + "'" +str(
            int(i[0])) + "'" + " where border_card=" + "'" +i[2] + "'" + ";"
        #print sql
        data = cur.execute(sql)
        conn.commit()
        print '返回数据:', data

    cur.close()
    conn.close()

if __name__ == '__main__':
    updateBorderInfo()
