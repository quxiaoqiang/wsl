#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
mailto_list=['quxiaoqiang@asean-go.com']     #收件人(list)
mail_host="smtp.163.com"                  #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="confidenceqxq@163.com"         #用户名
mail_pass="qq1050317987"                   #密码
mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com
def send_mail(to_list,sub,content):        #to_list是收件人列表，sub是邮件主题， content是
    me = 'confidenceqxq' + '<' + mail_user + '@' + mail_postfix + '>'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                            #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP(mail_host,25)
        server.login(mail_user,mail_pass)                    #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
for i in range(len(mailto_list)):                             #发送1封，上面的列表是几个人，这个就填几
    if send_mail(mailto_list,"你好","你好"):  #邮件主题和邮件内容
        print "done!"
    else:
        print "failed!"