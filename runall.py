import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from make import send_mail
import time,os
def send_mail(file_new):
    mail_from='xupeiqing1@163.com'#邮件发送地址
    mail_to='1205116977@qq.com'#邮件接收地址
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['From']=mail_from
    msg['To']=mail_to
    msg['Subject']=u"自动化测试报告"
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('xupeiqing1@163.com','xu0101qing')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print("发送邮件成功")
def send_report(testreport):
    result_dir = testreport
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    file_new = os.path.join(result_dir,lists[-1])
    print(file_new)
    send_mail(file_new)
def creatsuite():
    testunit=unittest.TestSuite()
#定义测试文件查找的目录
    test_dir=os.path.join(os.getcwd(),'testcases')
#定义 discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
#discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print(test_case)
        testunit.addTests(test_case)
    return testunit
now = time.strftime("%Y-%m-%d %H_%M_%S")
testfile=os.path.join(os.getcwd(),'report')
print(testfile)
filename = testfile+'\\'+now+'result.html'
fp = open(filename, 'wb+')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')
if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
    send_report(testfile)
