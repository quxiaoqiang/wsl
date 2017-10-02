#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import xlrd

def read_xls():
    server_name_port = []
    workbook = xlrd.open_workbook('./deploy.xlsx')
    count = len(workbook.sheets())

    for i in range(count):
        t = workbook.sheet_by_index(i)
        for k in range(t.nrows):
            ser = t.row_values(k, 0, 2)
            if ser[1] != '-' and ser[1] != '':
                server_name_port.append(ser)
    return server_name_port

if __name__ == '__main__':
    print read_xls()

