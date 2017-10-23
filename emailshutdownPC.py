import os
import time
import email
import poplib
import sys
import math
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.header import decode_header

#设置的参数登录帐号 邮箱 密码
smtpserver = 'smtp.163.com'    #发邮件邮箱服务
poplibserver = 'pop.163.com'    #查看邮件服务
sender = 'xxxxxxxxx@163.com' # 邮件登陆着，发件人
passwd =  'xxxxxx' # 登录邮件的授权密码
receive = 'xxxxxxxx@163.com' #接受者的邮箱，换成列表就可以多个发送

#设置发送内容的
emailsubject = '重置获取命令的选项，不做任何的操作'
emailtitle = 'this is meishayong email'
#构造一封邮件
message = MIMEText(emailtitle, 'plain', 'utf-8') #plain文本的格式
message['Subject'] = Header(emailsubject, 'utf-8')
message['From'] = sender
message['To'] = receive

# print(message.as_string())
#登录邮箱，给本邮箱发送邮件一封
smtp = SMTP_SSL(smtpserver) #连接到服务器
smtp.login(sender,passwd)   #登录到邮箱
smtp.sendmail(sender, receive, message.as_string())
smtp.quit()

while True:
    # 登录邮件获取第一封邮件的主题内容
    reademail = poplib.POP3(poplibserver)
    reademail.user(sender)
    reademail.pass_(passwd)
    Allemial = reademail.stat()
    newemail = reademail.top(Allemial[0], 0)
    emaillist = []
    for i in newemail[1]:
        emaillist.append(i.decode())
        try:
            emaillist.append(i.decode('gbk'))
        except:
            emaillist.append(i.decode('big5'))
    emaillistadd = email.message_from_string('\n'.join(emaillist))
    emailSublist = decode_header(emaillistadd['Subject'])
    def Getobject():
        if emailSublist[0][1]:
            getsubject = emailSublist[0][0].decode(emailSublist[0][1])
        else:
            getsubject = emailSublist[0][0]
        return getsubject
    getobject = Getobject()

    print("*********************寻找主题******************")
    print("**                                          **")
    print("**                                          **")
    print('  找到主题；' + getobject)
    print("**                                          **")
    print("**                                          **")
    cmd = getobject
    if cmd == "关机":
        os.system('shutdown -s -t 120 ')
    elif cmd == "不关机":
        print('不关机了')
        os.system('shutdown -a')
    print('********************等待时间中*****************')
    print("**                                          **")
    print("**                                          **")
    # time.sleep(3)
    for i in range(101):
        s = '| '
        y = '  '
        j = math.ceil(i/10)-1
        q = 10-j
        output = '进行更新时间:'+ str(i) + '%' + '   ['+ s * j + y * q + '] 继续' + '\r'
        sys.stdout.writelines(output)
        time.sleep(36)
    os.system('cls')



