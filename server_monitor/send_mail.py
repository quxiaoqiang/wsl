#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

def send_mail(to_list):
    sender = 'confidenceqxq@163.com'#'confidenceqxq@163.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
    mail_pass = "1050317987"  # 密码
    ret=True
    try:
        msg=MIMEText('服务偷停了','plain','utf-8')
        msg['From']=formataddr(["quxiaoqiang",sender])  #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["QXQ",user])  #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="服务崩溃了，你还睡觉？" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.aliyun.com",25) #发件人邮箱中的SMTP服务器，端口是25
        a = server.login(sender,mail_pass)  #括号中对应的是发件人邮箱账号、邮箱密码
        print server, a
        server.sendmail(sender,to_list,msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  #这句是关闭连接的意思
    except Exception, e:  #如果try中的语句没有执行，则会执行下面的ret=False
        print str(e)
        ret=False
    return ret



if __name__ == "__main__":
    user = 'quxiaoqiang@asean-go.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量
    if send_mail('quxiaoqiang@asean-go.com'):
        print 'ok'
    else:
        print 'fff'
'''


    for i in range(2):
        ret=send_mail(user)
        time.sleep(3)
        if ret:
            print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
        else:
            print("failed") #如果发送失败则会返回filed
'''
