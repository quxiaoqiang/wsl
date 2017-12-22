#!/usr/bin/env python
# _*_ coding: utf-8 _*

from Tkinter import *


def processQuit():
    print '退出'
    window.quit()
def processConfirm():
    a = (float(var1.get())-float(var0.get()))*float(var2.get())
    if var3.get() == 0:
        b = '不需要发票'
        c = a
    else:
        b = '需要发票'
        c = a - (float(var1.get())*float(var2.get())/1.03)*0.0468

    resultText.delete(0.0,END)  #清除文本框内容，重新打印
    resultText.insert(INSERT, '商品供应价格：'+var0.get()+' 元\n'+'商品采购价格：'+var1.get()+' 元\n'+
                      '边民采购数量：'+var2.get()+'\n'+'是否需要发票：'+b+'\n')
    resultText.insert(INSERT, '边民收益：' + str(c) + '\n')
    resultText.insert(INSERT, '\n')
    resultText.focus_force()

    print '商品供应价格：%s\n商品采购价格：%s\n边民采购数量：%s\n是否需要发票：%s\n边民收益：%s\n' \
          % (var0.get(), var1.get(), var2.get(), b, c)

window = Tk()
window.title('计算边民收益')
window.geometry('700x400')
window.resizable(width=True, height=True)

frame1 = Frame(window)  # 创建一个框架
frame1.pack()  # 将框架frame1放置在window中

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

#供应商发布商品价格
supportorPrice = Label(frame1, text='商品供应价格:', font=('Arial', 16))
valueEntry1 = Entry(frame1, textvariable = var0)

#采购商购买价格
buyerPrice = Label(frame1, text='商品采购价格:', font=('Arial', 16))
valueEntry2 = Entry(frame1, textvariable = var1)

#边民采购商品数量
borderCount = Label(frame1, text='边民采购数量:', font=('Arial', 16))
valueEntry3 = Entry(frame1, textvariable = var2)

#边民采购商品数量
var3 = IntVar()
bill = Label(frame1, text='是否需要发票:', font=('Arial', 16))
needPill = Radiobutton(frame1, text='需要发票', value=1, variable = var3)
noNeedPill = Radiobutton(frame1, text='不需要发票', value=0,variable = var3)

#按钮
confimButton = Button(frame1, text='确定', command=processConfirm)
confimButton.pack()
quitButton = Button(frame1, text='退出', command=processQuit)
quitButton.pack()

#gride布局
supportorPrice.grid(row=1, column=1)
valueEntry1.grid(row=1, column=2)

buyerPrice.grid(row=2, column=1)
valueEntry2.grid(row=2, column=2)

borderCount.grid(row=3, column=1)
valueEntry3.grid(row=3, column=2)

bill.grid(row=4, column=1)
needPill.grid(row=4, column=2)
noNeedPill.grid(row=4, column=3)

confimButton.grid(row=5, column=1)
quitButton.grid(row=5,column=2)

#计算结果
resultText = Text(window, bg='grey',width=45,height=10,font=('Arial', 18))
resultText.pack()

window.mainloop()

