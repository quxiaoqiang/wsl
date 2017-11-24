#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import commands

# 返回命令执行结果
def getComStr(comand):
    global proStr
    try:
        stat, proStr = commands.getstatusoutput(comand)
    except:
        print "command %s execute failed, exit" % comand
    # 将字符串转化成列表
    #proList = proStr.split("\n")
    return proStr

def filterList():
    '''
    tmpStr = getComStr("netstat -tpln")
    tmpList = tmpStr.split("\n")
    del tmpList[0:2]
    newList = []
    for i in tmpList:
        val = i.split()
        del val[0:3]
        del val[1:3]
        del val[0:2]
      '''
    newList = []
    a = [['(only'], ['Local', 'Address', 'State', 'PID/Program', 'name'], ['0.0.0.0:45419', '32536/java'],
         ['0.0.0.0:8300', '32644/java'], ['0.0.0.0:35532', '-'], ['0.0.0.0:3181', '32536/java'],
         ['0.0.0.0:5006', '1130/java'], ['0.0.0.0:8910', '443/java'], ['0.0.0.0:9999', '1130/java'],
         ['0.0.0.0:8080', '31828/java'], ['120.77.71.43:9200', '31501/java'], ['10.27.203.5:3889', '32536/java'],
         ['0.0.0.0:8019', '32644/java'], ['120.77.71.43:9300', '31501/java'], ['0.0.0.0:22', '-'],
         ['0.0.0.0:5111', '1130/java'], ['0.0.0.0:40376', '31937/java'], ['0.0.0.0:5016', '31828/java'],
         ['0.0.0.0:8282', '-'], ['127.0.0.1:8091', '443/java'], ['127.0.0.1:8059', '32644/java'],
         ['0.0.0.0:37052', '32111/java'], ['0.0.0.0:6400', '31937/java'], ['0.0.0.0:9092', '32111/java']]

    del a[0:2]

    for i in a:
        if '-' not in i:
            tmpList1 = i[0].split(':')
            tmpList2 = i[1].split('/')

            newList.append(tmpList1[1])
            newList.append(tmpList2[-1])
    return newList

print filterList()


