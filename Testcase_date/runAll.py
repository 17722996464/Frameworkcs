import os
import HTMLTestRunner
from Testcase_date.getpathInfo import getpathInfo
from Common.config_Email import SendMail
import unittest
from Testcase_date.readConfig import ReadConfig
#from Common.log import Logger
import Common.log
log=Common.log.logger
path=getpathInfo().get_Path()
print(path)
#path1= 'D:\zz\Framework'
#print(path)
report_path = os.path.join(path,'result')
print(report_path)
class AllTest():
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path, 'report.html')
        print(resultPath)
        self.casesListFile = os.path.join(path, "caselist.txt")
        print(self.casesListFile)
        self.caseFile ='D:\zz\Framework\Testcase'
        self.caseList = []
        log.info('resultPath'+resultPath)
        log.info('caseListFile'+self.casesListFile)
        log.info('caseList'+str(self.caseList))



    def set_case_list(self):
        """
                    读取caselist.txt文件中的用例名称，并添加到caselist元素组
                    :return:
                    """
        fb = open(self.casesListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()


    def set_case_suite(self):
        """
                        :return:
                        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py',
                                                           top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            #print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集


    def run(self):
        """
                        run test
                        :return:
                        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
           # print('try')
           # print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
               # print('if-suit')
                fp = open(resultPath,'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                 #调用HTMLTestRunner
                HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口自动化测试',description='作者：周周').run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            print("*********TEST END*********")
            # log.info("*********TEST END*********")
            #fp.close()
            m = SendMail(
                username=ReadConfig().get_email('username'),
                passwd=ReadConfig().get_email('passwd'),
                recv=['zhoujun@163.net','1130394994@qq.com','15769394781@163.com'],
                title=ReadConfig().get_email('title'),
                content=ReadConfig().get_email('content'),
                #file=r'E:\\testpy\\python-mpp\\day7\\作业\\data\\mpp.xls',
            )
            m.send_email()
            print( ReadConfig().get_email('recv'))


if __name__ == '__main__':
    AllTest().run()