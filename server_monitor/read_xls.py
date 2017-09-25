#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import xlrd

workbook = xlrd.open_workbook('./deploy.xlsx')
sheet_names = workbook.sheet_names()


print '---------------------------------------'

for sheet_name in sheet_names:
    print '表格名称:',sheet_name

    sheet = workbook.sheet_by_name(sheet_name)
    rows = sheet.nrows
    cols = sheet.ncols
    print rows,cols