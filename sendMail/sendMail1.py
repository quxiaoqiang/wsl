#!/usr/bin/env python
# coding=utf-8
import smtplib
from email import MIMEText
from email import MIMEMultipart
from email import MIMEBase
from email import Encoders
import time


mail_body = 'hello, this is the mail content'
mail_from = ''  # 发件人的邮箱
mail_to = ['']  # 收件人邮箱
# 构造MIMEMultipart对象做为根容器
msg = MIMEMultipart()

# 构造MIMEText对象做为邮件显示内容并附加到根容器
body = MIMEText(mail_body)
msg.attach(body)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
# 等同于如下3行
# contype = 'application/octet-stream'
# maintype, subtype = contype.split('/', 1)
# part = MIMEBase(maintype, subtype)
part = MIMEBase('application', 'octet-stream')

# 读入文件内容并格式化，此处文件为当前目录下，也可指定目录 例如：open(r'/tmp/123.txt','rb')
part.set_payload(open('123.txt', 'rb').read())
Encoders.encode_base64(part)
## 设置附件头
part.add_header('Content-Disposition', 'attachment; filename="herb.zip"')
msg.attach(part)

# 设置根容器属性
msg['Subject'] = 'this is the title'
msg['From'] = mail_from
msg['To'] = ';'.join(mail_to)
msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
# 如上得到了格式化后的完整文本msg.as_string()
# 用smtp发送邮件
smtp = smtplib.SMTP()
smtp.connect('')  # 服务，如果是163的邮箱，就填上smtp.163.com
smtp.login('发件的邮箱', '发件的密码')
smtp.sendmail(mail_from, mail_to, msg.as_string())
smtp.quit()
print 'ok'