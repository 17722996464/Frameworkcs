import smtplib
import base64
from email.mime.multipart import MIMEMultipart
import os
from Testcase_date.getpathInfo import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
from email.mime.text import MIMEText
from Testcase_date.readConfig import ReadConfig
path=getpathInfo().get_Path()
print(path)
mail_path = os.path.join(path, 'result', 'report.html')#获取测试报告路径
"""class send_email():
    def EMAIL(self):
        mailserver = "smtp.163.com"  #邮箱服务器地址
        username_send = 'jol@163.com'  #邮箱用户名
        password = 'zj123456'   #邮箱密码：需要使用授权码
        username_recv = '15769394781@163.com'#,'15769394781@163.com'  #收件人，多个收件人用逗号           a
        mail = MIMEMultipart()
        # file = r'E:\testpy\python-mpp\day8\\练习\\sendmail.py'
        # att = MIMEText(open(file,encoding='utf-8').read())  #这个只可以发送py或者txt附件，复杂一点的就会报错
        file=r'D:\zz\Framework\Testcase_date\result\report.html'
        att = MIMEText(open(file, 'rb').read(),"base64", "utf-8")  #这个可以发送复杂的附件，比如附件为表格
        att["Content-Type"] = 'application/octet-stream'
        #这行是把附件的格式进行一些处理，不知道为啥要这么写，但是如果不写接收到的附件已经不是表格样式了
        new_file='=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='
        att["Content-Disposition"] = 'attachment; filename="%s"'%new_file
        mail.attach(att)
        mail.attach(MIMEText('测试报告内容'))#邮件正文的内容
        mail['Subject'] = '周周接口自动化测试报告'
        mail['From'] = username_send  #发件人
        mail['To'] = username_recv  #收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
        att["Content-Disposition"] = 'attachment; filename="%s"'%new_file
        smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
        # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
        smtp.login(username_send,password)  #登录邮箱
        smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.quit() # 发送完毕后退出smtp
        print ('success')
                                                                
if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    #print(subject)
    send_email().EMAIL()
    print("send email ok!!!!!!!!!!")"""
class SendMail(object):
    def __init__(self,username,passwd,recv,title,content,file=None,email_host='smtp.163.com',port=25):
        self.username = ReadConfig().get_email('username') #用户名
        self.passwd = ReadConfig().get_email('passwd') #密码
        self.recv = ['zhoujun@163.net','1130394994@qq.com','15769394781@163.com']#15769394781@163.com#收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = ReadConfig().get_email('title') #邮件标题
        self.content = ReadConfig().get_email('content')#邮件正文
        self.file = 'D:\\zz\\Framework\\Testcase_date\\result\\report.html' #附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = "smtp.163.com" #smtp服务器地址
        self.port = 25 #普通端口
        #self.ssl = ssl #是否安全链接
        #self.ssl_port = 465 #安全链接端口
    def send_email(self):
        msg = MIMEMultipart()
        if self.file:#处理附件的
            file_name = os.path.split(self.file)[-1]#只取文件名，不取路径
        try:
            f = open(self.file, 'rb').read()
        except Exception as e:
            raise Exception('附件打不开！！！！')
        else:
            att = MIMEText(f,"base64", "utf-8")
            att["Content-Type"] = 'application/octet-stream'
            #base64.b64encode(file_name.encode()).decode()
            new_file_name='=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
            #这里是处理文件名为中文名的，必须这么写
            att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
            msg.attach(att)
            msg.attach(MIMEText(self.content))#邮件正文的内容
            msg['Subject'] = self.title  # 邮件主题
            msg['From'] = self.username  # 发送者账号
            msg['To'] = ','.join(self.recv)  # 接收者账号列表
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
            self.smtp.login(self.username,self.passwd)
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            print('发送成功！')
            #print(ReadConfig().get_email('recv'))
            self.smtp.quit() 
        """if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
            #发送邮件服务器的对象
            self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print('出错了。。',e)
        else:
            print('发送成功！')
            self.smtp.quit() """
#if __name__ == '__main__':# 运营此文件来验证写的se
    #print(subject)
    #SendMail().send_email()
    #print("send email ok!!!!!!!!!!")
if __name__ == '__main__':
    m = SendMail(
        username='jol@163.com',
        passwd='zj123456',
        recv='zhoujun@163.net',
        title='发送邮件20180205',
        content='测试发送邮件，qq发件，接收方一个是163邮箱，另一个是qq邮箱。20180205',
        file=r'D:\\zz\\Framework\\Testcase_date\\result\\report.html',
        #ssl=True,
    )
    m.send_email()