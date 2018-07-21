import time,os
#from cxcelparse import *
#..\\..\\webtest\\make

dirname=os.path.split(os.path.realpath(__file__))[0]
print("test"+dirname)
#导出文件路径
txt_path = os.path.join(dirname,"text.txt").replace("\\","\\\\")
print(txt_path)
#生成脚本文件路径
filename=os.path.join(dirname,"testcases\\").replace("\\","\\\\")
print("用例脚本路径："+filename)
#截图文件路径
path=os.path.join(dirname,"data\\").replace("\\","\\\\")
print("用例路径："+path)
pic_path=os.path.join(dirname,'pic\\').replace("\\","\\\\")
print("截图路径："+pic_path)
#测试报告路径
#report_path=os.path.join("\'"+dirname,'report\\\'+current_time+\'report.html'+"\'")
report_path=os.path.join(dirname,'report').replace("\\","\\\\")
print ('report_path is:'+report_path)
#测试报告标题
report_title='u\'自动化测试报告\','
#测试报告描述
report_des='u\'建信人寿官网测试\')'

t='\t'
tt='\t\t'
n='\n'
nn='\n\n'
