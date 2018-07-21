#coding=utf-8
import unittest, time, os, multiprocessing
import HTMLTestRunner
#查找多有含有thread的文件，文件夹
def EEEcreatsuit():
    #casedir=os.listdir('F:\\webtest\\testcases')
    suite=[]
    testunit=unittest.TestSuite()
#定义测试文件查找的目录
    test_dir=os.path.join(os.getcwd(),'testcases')
#定义 discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    suite.append(testunit)
    #print("===casedir:====",casedir)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("!!!suite:!!!",testunit)
    return suite,test_dir
#多线程运行测试套件，将结果写入HTMLTestRunner报告
def EEEEEmultiRunCase(suite,casedir):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    testfile=os.path.join(os.getcwd(),'report')
    filename = testfile+'\\'+now+'result.html'
    fp = open(filename, 'wb+')
    proclist=[]
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner( stream=fp, title=u'测试报告', description=u'用例执行情况：' )
        proc = multiprocessing.Process(target=runner.run(i),args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
        fp.close()
if __name__ == "__main__":
    runtmp=EEEcreatsuit()
    EEEEEmultiRunCase(runtmp[0],runtmp[1])
