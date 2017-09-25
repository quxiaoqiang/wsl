#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'''从excel读取数据'''

import xlrd,json

'''
['Book', 'FMLA_TYPE_ARRAY', 'FMLA_TYPE_CELL', 'FMLA_TYPE_COND_FMT', 'FMLA_TYPE_DATA_VAL', 'FMLA_TYPE_NAME','xldate',
 'FMLA_TYPE_SHARED', 'MMAP_AVAILABLE', 'USE_MMAP', 'X12Book', 'XLDateError', 'XLRDError', 'XL_CELL_BLANK',
  'XL_CELL_BOOLEAN', 'XL_CELL_DATE', 'XL_CELL_EMPTY', 'XL_CELL_ERROR', 'XL_CELL_NUMBER', 'XL_CELL_TEXT','sys',
  '__VERSION__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'biff_text_from_num',
  'biffh', 'book', 'cellname', 'cellnameabs', 'colname', 'compdoc', 'count_records', 'decompile_formula', 'dump',
  'dump_formula', 'empty_cell', 'error_text_from_code', 'evaluate_name_formula', 'formatting', 'formula', 'info',
  'licences', 'mmap', 'oBOOL', 'oERR', 'oNUM', 'oREF', 'oREL', 'oSTRG', 'oUNK', 'okind_dict', 'open_workbook', 'path',
  'pprint', 'rangename3d', 'rangename3drel', 'sheet', 'timemachine', 'xldate_as_tuple', 'xlsx', 'zipfile']
'''

sheet = xlrd.open_workbook('/Users/QXQ/Desktop/2017.5.31.xlsx')
table = sheet.sheet_by_index(0)
rows = table.nrows
cols = table.ncols

print rows,cols
a = table.row_values(2)
print