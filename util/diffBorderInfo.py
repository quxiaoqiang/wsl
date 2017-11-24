#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import xlrd

excel = xlrd.open_workbook('./border.xls')
book = excel.sheet_by_index(0)
print (book.nrows)

list = []
list1 = []
for i in range(1,4174):
    list.append(book.row_values(i))

for i in range(0,4173):
    mysql = "insert into border_info values("+"'"+str(list[i][0])+"','"+str(list[i][1])+"','"+str(list[i][2])+"','"+str(list[i][3])+"','"+str(list[i][4])+"');"
    print (mysql)


