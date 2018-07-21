import sys,os,time
from make.maker import *
from config import *
class RunTest:
    def runalltest(self):
        for file in os.walk(path):
            file_name = list(file)[2]
            #print(file_name)
            #print(str(file_name).split('.'))
            for i in file_name:
                #print(str(i).split('.'))
                if str(i).split('.')[1]=='xlsx':
                    print("***************")
                    print (str(i))
                    run = Runtest(str(i))
                    run.runtest()
                    #time.sleep(5)
    def runsingletest(self,excel_name):
        run = Runtest(excel_name)
        run.runtest()
        
if __name__ == '__main__':
	RunTest().runalltest()
	#RunTest().runsingletest('e行无忧天天保.xlsx')
