#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from xlrd import *

def readExcel():
    list = []
    excel  = open_workbook(filename='border1022.xls')
    book0 = excel.sheet_by_index(0)
    #print book0.nrows,book0.ncols

    for i in range(1,book0.nrows):
        list.append(book0.row_values(i,0,book0.ncols))
    return list

if __name__ == '__main__':
    for i in readExcel():
        print i[0]