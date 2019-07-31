import json
import unittest
from Common.config_Http import RunMain
import paramunittest
from Testcase_date.geturlparams import geturlParmes
import urllib.parse
from Testcase_date.readExcel import readExcel
url = geturlParmes().get_url()# 调用我们的geturlParams获取我们拼接的URL
#print(url)
login_xls = readExcel().get_xls('zj.xlsx','ww')
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query=str(query)
        self.method=str(method)

    def description(self):
        self.case_name
    def setUp(self):
        print(self.case_name+'测试前开始准备')
    def testcase01(self):
        self.checkResult()
    def tearnDown(self):
        print('测试结束，输出log完结\n\n')
    def checkResult(self): #断言
        #url1=geturlParams().get_url('new_url')
        new_url1=url+self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url1).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
         #print(dict.get('name'))
        info= RunMain().run_main(self.method,url,data1)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss=json.loads(info)# 将响应转换为字典格式
        if self.case_name=='login':
             self.assertEqual(ss['code'],200)# 如果case_name是login，说明合法，返回的code应该为200
        if self.case_name == 'login_error':
             self.assertEqual(ss['code'],-1)
        if self.case_name=='login_null':
             self.assertEqual(ss['code'],10001)
if __name__=="__main__":
    print(url)