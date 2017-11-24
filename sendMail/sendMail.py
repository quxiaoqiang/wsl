#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

class Mailer(object):
    def __init__(self, maillist, mailtitle, mailcontent, acclist):
        self.mail_list = maillist
        self.mail_acc = acclist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = "smtp.mxhichina.com"
        self.mail_user = "quxiaoqiang@asean-go.com"
        self.mail_pass = "Qq1050317987"
        self.mail_postfix = "asean-go.com"

    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        #me = self.mail_user
        msg = MIMEMultipart()
        msg['Subject'] = '测试python发送邮件'
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)
        msg['Cc'] = ";".join(self.mail_acc)

        #puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        puretext = MIMEText('你好 ' + self.mail_content, 'plain', 'utf-8')
        msg.attach(puretext)

        # jpg类型的附件
        #jpgpart = MIMEApplication(open('/home/mypan/1949777163775279642.jpg', 'rb').read())
        #jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
        #msg.attach(jpgpart)

        # 首先是xlsx类型的附件
        xlsxpart = MIMEApplication(open('deploy.xlsx', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='deploy.xlsx')
        msg.attach(xlsxpart)

        # zip类型的附件
        zippart = MIMEApplication(open('abc.zip', 'rb').read())
        zippart.add_header('Content-Disposition', 'attachment', filename='abc.zip')
        msg.attach(zippart)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.mail_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.mail_user, self.mail_pass)  # 登录到你邮箱
            s.sendmail(me, self.mail_list + self.mail_acc, msg.as_string())  # 发送内容
            time.sleep(2)
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False

if __name__ == '__main__':
    # send list
    mailto_list = ["quxiaoqiang@asean-go.com", "confidenceqxq@163.com"]
    mailto_cc = ["1050317987@qq.com", "quxiaoqiang0566@dingtalk.com"]
    mail_title = '这是邮件标题'
    mail_content = '这是邮件正文内容'
    mm = Mailer(mailto_list, mail_title, mail_content, mailto_cc)
    res = mm.sendMail()
    print '结果：', res