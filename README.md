# Emailshutdown
____
###前言###
>　　自从爱上Python后，觉得这门语言真的是太方便了，他的设计极大的增强了代码的可读性，学习起来也更加平缓，可以很快的具备生产力，现在只要看到能批量操作的东西，都想用代码来将他实现。要成为专家还是要深入的学习才行，而不是像我这样乱搞，乱搞，乱搞。
　　python不仅是一个完成工作的工具，而且还是非常享受他的编程的过程。在前几篇的文章中，其中有一篇是个关于搭建Ubuntu邮件服务器，来进行一系列的操作，是为了不消耗我自己，这里还要对邮件在进行编辑，完成远程一键关机，这个关机使用邮件而不是远程的连接。 
　　为什么会有这个想法呢？原因是我晚上在实验室学习一半的时候，出去去吃饭，然后就不不想回去了，或者去上课的时候没关电脑（当时想着我一定还能回来在学会，结果就直接的玩去了。什么学习都抛到脑后）这样一来电脑就会在LAB咆哮一夜，不仅浪费电，还伤害我的电脑，然后就傻傻给别人发短信，帮我把电脑管了吧!这样感觉不仅麻烦自己，还麻烦别人。于是想到这python的功能，做一个关闭计算机的程序。

　　然后我教大家怎么装逼：在一堆朋友聊天的时候，忽然说：哎呀！我的电脑在那那忘了关机了，你手机借我一下，我关个机。然后就发送一个邮件，电脑管了，再说:好了，电脑关了。这之后就可以讲讲你是怎样做到的。OR，在大冬天的时候，再和你女朋友讨论是谁下床去把电脑关了的时候，就又是装逼的时候了。这个时候就会带来满满 的羡慕之情。


___
###预期达成效果###

通过用手机，或者电脑发送一份邮件给我的邮箱，电脑过一段时间自己关机。这个装逼的程度不下于神舟上天。

**演示**

![快进了30倍的Gif](http://upload-images.jianshu.io/upload_images/6967995-4b31f8e9053f4a7c.gif?imageMogr2/auto-orient/strip)

___

###执行计划###

用python写下一串代码
邮件开启授权客户端密码和pop3&smtp

___

###smtp和pop###

**SMTP**(Simple Mail Transfer Protoco)简单邮件传输协议
*　　SMTP是一个相对简单的基于[文本](https://zh.wikipedia.org/wiki/%E6%96%87%E6%9C%AC)的[协议](https://zh.wikipedia.org/wiki/TCP/IP%E5%8D%8F%E8%AE%AE)。在其之上指定了一条[消息](https://zh.wikipedia.org/wiki/%E6%B6%88%E6%81%AF)的一个或多个接收者（在大多数情况下被确认是存在的），然后消息文本会被传输。可以很简单地通过[telnet](https://zh.wikipedia.org/wiki/Telnet)程序来测试一个SMTP服务器。SMTP使用[TCP](https://zh.wikipedia.org/wiki/TCP)端口25。要为一个给定的域名决定一个SMTP服务器，需要使用MX (Mail eXchange) [DNS](https://zh.wikipedia.org/wiki/DNS)。
在八十年代早期SMTP开始被广泛地使用。当时，它只是作为[UUCP](https://zh.wikipedia.org/wiki/UUCP)的补充，UUCP更适合于处理在间歇连接的机器间传送邮件。相反，SMTP在发送和接收的机器在持续连接的网络情况下工作得最好。
[Sendmail](https://zh.wikipedia.org/wiki/Sendmail)是最早使用SMTP的邮件传输代理之一。到2001年至少有50个程序将SMTP实现为一个客户端（消息的发送者）或一个服务器（消息的接收者）。一些其他的流行的SMTP服务器程序包括了Philip Hazel的exim，[IBM](https://zh.wikipedia.org/wiki/IBM)的Postfix， [D. J. Bernstein](https://zh.wikipedia.org/w/index.php?title=D._J._Bernstein&action=edit&redlink=1)的[Qmail](https://zh.wikipedia.org/wiki/Qmail)，以及[Microsoft Exchange Server](https://zh.wikipedia.org/wiki/Microsoft_Exchange_Server)。
由于这个协议开始是基于纯[ASCII](https://zh.wikipedia.org/wiki/ASCII)文本的，它在[二进制](https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%BF%9B%E5%88%B6)文件上处理得并不好。诸如[MIME](https://zh.wikipedia.org/wiki/MIME)的标准被开发来编码二进制文件以使其通过SMTP来传输。今天，大多数SMTP服务器都支持8位MIME扩展，它使二进制文件的传输变得几乎和纯文本一样简单。
SMTP是一个“推”的协议，它不允许根据需要从远程服务器上“拉”来消息。要做到这点，邮件客户端必须使用[POP3](https://zh.wikipedia.org/wiki/%E9%83%B5%E5%B1%80%E5%8D%94%E5%AE%9A)或[IMAP](https://zh.wikipedia.org/wiki/IMAP)。另一个SMTP服务器可以使用ETRN在SMTP上触发一个发送。*
--参考[wiki](https://zh.wikipedia.org/wiki/%E7%AE%80%E5%8D%95%E9%82%AE%E4%BB%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)百科

**POP**(Post Office Protocol)邮局协议
*　　是[TCP/IP](https://zh.wikipedia.org/wiki/TCP/IP)协议族中的一员，由RFC 1939定义。本协议主要用于支持使用[客户端](https://zh.wikipedia.org/wiki/%E5%AE%A2%E6%88%B7%E7%AB%AF)远程管理在[服务器](https://zh.wikipedia.org/wiki/%E6%9C%8D%E5%8A%A1%E5%99%A8)上的[电子邮件](https://zh.wikipedia.org/wiki/%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6)。最新版本为**POP3**，全名“Post Office Protocol - Version 3”，而提供了[SSL](https://zh.wikipedia.org/wiki/SSL)加密的POP3协议被称为**POP3S**。
POP支持[离线](https://zh.wikipedia.org/wiki/%E5%9C%A8%E7%BA%BF%E5%92%8C%E7%A6%BB%E7%BA%BF)邮件处理。其具体过程是：邮件发送到服务器上，电子邮件客户端调用邮件客户机程序以连接服务器，并下载所有未阅读的电子邮件。这种离线访问模式是一种存储转发服务，将邮件从邮件服务器端送到个人[终端](https://zh.wikipedia.org/wiki/%E7%B5%82%E7%AB%AF)机器上，一般是[PC](https://zh.wikipedia.org/wiki/PC)机或MAC。一旦邮件发送到PC机或[MAC](https://zh.wikipedia.org/wiki/Macintosh)上，邮件服务器上的邮件将会被删除。但目前的POP3邮件服务器大都可以“只下载邮件，服务器端并不删除”，也就是改进的POP3协议。*
--参考[wiki](https://zh.wikipedia.org/wiki/%E9%83%B5%E5%B1%80%E5%8D%94%E5%AE%9A)百科
　　简单来说，SMTP是发送邮件， POP3/IMAP管是接受邮件,相当于中转站，将邮件发送到客户端。SMTP 认证，简单地说就是要求必须在提供了账户名和密码之后才可以登录 SMTP 服务器，这就使得那些垃圾邮件的散播者无可乘之机。 
　　增加 SMTP 认证的目的是为了使用户避免受到垃圾邮件的侵扰。SMTP service收到邮件后转给负责接收邮件的POP3 service，POP3是把邮件下载到本地计算机,不与服务器同步。它规定怎样将个人计算机连接到Internet的邮件服务器和下载电子邮件的电子协议。它是因特网电子邮件的第一个**离线**协议标准,POP3允许用户从服务器上把邮件存储到本地主机（即自己的计算机）上,同时删除保存在邮件服务器上的邮件，而POP3服务器则是遵循POP3协议的接收邮件服务器，用来接收电子邮件的。
　　说到POP3也要说一下IMAP虽然这里用不到，pop3是静态，IMAP是动态。IMAP提供Webmail 与电子邮件客户端之间的双向通信，客户端收取的邮件仍然保留在服务器上，同时在客户端上的操作都会反馈到服务器上（如：删除邮件，标记已读等，服务器上的邮件也会做相应的动作。所以无论从浏览器登录邮箱或者客户端软件登录邮箱，看到的邮件以及状态都是一致的。）。而POP3在客户端的操作不会反馈到服务器上。

　　网易邮箱已经默认开启 POP3/SMTP/IMAP 服务，方便您可以通过电脑客户端软件更好地收发邮件,但是客户端的授权密码需要自己手机开通，如何开通参见小弟的另一个小弟的[另一个文章](http://www.jianshu.com/p/d8595fd6b069)介绍获取授权码。
![网易163相关服务信息](http://upload-images.jianshu.io/upload_images/6967995-da5ac359658a6567.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
___
###实现过程
　　当程序运行的时候，先对163邮箱发送一封自己构建的邮件，避免因上次自动化关机导致运行程序立刻关机。
　　用手机或其他设备对邮箱发送关闭电脑文字，邮箱读取主题文字为关机命令，执行关闭电脑命令，完成操作。将其打包成windows下可执行文件，电脑运行。
　　另外可讲sleep设置时间间断缩小，来达到秒响应的效果。

**设置参数**


    #设置的参数登录帐号 邮箱 密码
    smtpserver = 'smtp.163.com'    #发邮件邮箱服务
    poplibserver = 'pop.163.com'    #查看邮件服务
    sender = 'xxxxxxxxx@163.com' # 邮件登陆着，发件人
    passwd =  '****** # 登录邮件的授权密码
    receive = 'xxxxxxxxx@163.com' #接受者的邮箱，换成列表就可以多个发送

**构造一封邮件发送**
 
    #设置发送内容的
    emailsubject = '重置获取命令的选项，不做任何的操作'
    emailtitle = 'this is meishayong email'
    #构造一封邮件
    message = MIMEText(emailtitle, 'plain', 'utf-8') #plain文本的格式
    message['Subject'] = Header(emailsubject, 'utf-8')
    message['From'] = sender
    message['To'] = receive

    #print(message.as_string())
    #登录邮箱，给本邮箱发送邮件一封
    smtp = SMTP_SSL(smtpserver) #连接到服务器
    smtp.login(sender,passwd)   #登录到邮箱
    smtp.sendmail(sender, receive, message.as_string())
    smtp.quit()


**登录邮箱获取邮箱内容**


    # 登录邮件获取第一封邮件的主题内容
    reademail = poplib.POP3(poplibserver)#连接到POP3服务器
    reademail.user(sender)
    reademail.pass_(passwd)
    Allemial = reademail.stat()
    newemail = reademail.top(Allemial[0], 0)#获取邮件中的第一封邮件主题
    emaillist = []
    for i in newemail[1]:      #邮件 主题的编码格式
        emaillist.append(i.decode())
        try:
            emaillist.append(i.decode('gbk'))
        except:
            emaillist.append(i.decode('big5'))
    emaillistadd = email.message_from_string('\n'.join(emaillist))
    emailSublist = decode_header(emaillistadd['Subject'])
    def Getobject():   #获得邮件主题
        if emailSublist[0][1]:
            getsubject = emailSublist[0][0].decode(emailSublist[0][1])
        else:
            getsubject = emailSublist[0][0]
        return getsubject
    getobject = Getobject()

**执行关机命令**


    print("*********************寻找主题******************")
    print("**                                          **")
    print("**                                          **")
    print('  找到主题；' + getobject)
    print("**                                          **")
    print("**                                          **")
    cmd = getobject
    if cmd == "关机":
        os.system('shutdown -s -t 120 ')   #执行关机命令
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
        sys.stdout.writelines(output) #进行输出且不换行
        time.sleep(36)
    os.system('cls')#清屏处理




____

###代码###



[github](https://github.com/Hatcat123/Emailshutdown)

###总结###

冲动的想法构建了此项应用，为了好玩和方便自己，代码写的不够pythonic，还希望你多多包涵。转载使用的时候请获得作者同意，也欢迎你的赞赏。