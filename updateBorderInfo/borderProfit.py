#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Tkinter import *
import tkMessageBox


'''
边民采购额 = 边民交易数量 * 供应商销售价格
边民销售额 = 边民交易数量 * 采购商采购价格
交易利润 = 边民销售额 – 边民采购额
交易增值税 = （边民销售额/1+3%）* 4.68%【增值税率】）
边民收入 = 交易利润 - 交易增值税
备注：边民收入 >= 30 才能进行交易
'''
# 供应价
price_supply =9.8
# 采购价
price_purchase =10.3
# 商品规格
item_specifications =19
# 交易商品总件数
quantity = 42
# 商品数量(规格*件数)
count = item_specifications * quantity
# 增值税率
tariff = 0.0468

b_pur = price_supply * count # 边民购买商品支出
b_sup = price_purchase * count # 边民销售商品收入
profit = b_sup - b_pur # 边民毛收入
tax = (b_sup/(1+0.03)) * tariff #边民交易增值税
b_profit = profit - tax #边民纯收入


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.name = Entry(self)
        self.name.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
