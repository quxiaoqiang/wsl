#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from xlrd import *


e = open_workbook(filename='./goods.xlsx')

#print '行数:', e.sheet_by_index(0).nrows
#print '列数:', e.sheet_by_index(0).ncols

book1 = e.sheet_by_index(0)

list = [1,2]
rows_value = []     #编号/商品名称/计量单位/价格（单位：元）/海关分类/电商一级/电商二级
for row_index in range(book1.nrows):
    rows_value.append(book1.row_values(row_index))
    #print rows_value[row_index]

for i in rows_value[0]:
    print i

