#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
* 边民：
边民采购额 = 边民交易数量 * 供应商销售价格
边民销售额 = 边民交易数量 * 采购商采购价格
交易利润 = 边民销售额 – 边民采购额
交易增值税 = （边民销售额 / 1+3 % ） * 4.68 % 【增值税率】）
边民收入 = 交易利润 - 交易增值税
备注：边民收入 >= 30 才能进行交易

'''
sell_price = float(raw_input('请输入商品供应价格：'))
buy_price = float(raw_input('请输入商品采购价格：'))
count = float(raw_input('请输入边民交易数量：'))
border_buy = count * sell_price
border_sell = count * buy_price

#是否需要发票
bill = str(raw_input('请选择是否需要发票 1.需要,2.不需要：'))
if bill== '1':
    print '您的选择是需要发票'
    tax = (border_sell/(1+0.03)) * 0.0468
else:
    print '您的选择是不需要发票'
    tax = (border_sell/(1+0.03)) * 0

#边民收入
border_recevie = border_sell - border_buy - tax

print '边民采购%skg商品,预计收入%s' %(count,border_recevie)


