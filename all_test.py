#coding=utf-8
import unittest
import HTMLTestRunner
import os ,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#定义发送邮件
def sentmail(file_new):
#发信邮箱
    mail_from='jifengxiaoyue1@126.com'
#收信邮箱
    mail_to='jifengxiaoyue1@126.com'
#定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
#定义标题
    msg['Subject']=u"百度测试报告"
#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
#连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.126.com')
#用户名密码
    smtp.login('jifengxiaoyue1@126.com','xin890205')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'E:/pythonproject/baidu/report/'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"/"+fn) if not
os.path.isdir(result_dir+"/"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-2])
#找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print file_new
#调用发邮件模块
    sentmail(file_new)

'''import sys
sys.path.append('E:/pythonproject/baidu/test_baidu')
from test_baidu import*
#这里需要导入测试文件
import test_baiduchangewindow,test_baidusearch
import HTMLTestRunner
import time,os
import allcase_list #调用数组文件

#获取数组方法
alltestnames = allcase_list.caselist()

#创建测试套件
testunit=unittest.TestSuite()
#循环读取数组中的用例
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))
'''
#把 test_baidu 目录添加到 path 下，这里用的相对路径
listaa = 'E:/pythonproject/baidu/test_baidu'
def creatsuitel():
    testunit = unittest.TestSuite()
#discover 方法定义
    discover=unittest.defaultTestLoader.discover(listaa,
        pattern ='start_*.py',
        top_level_dir=None)
#discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit
alltestnames = creatsuitel()


#取当前时间
now=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

#定义个报告存放路径，支持相对路径。
filename = "E:/pythonproject/baidu/report/"+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

#执行测试套件
#runner = unittest.TextTestRunner()
if __name__ == "__main__":
    # 执行测试用例
    runner.run(alltestnames)
    # 执行发邮件
    sendreport()
