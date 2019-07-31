import requests
import json

class RunMain():

    def send_post(self,url,data): #定义一个方法，传入需要的url和data
        result =  requests.post(url=url,data=data).json()#url和data参数动态化
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)#请求结果转换成字符串形式
        return res

    def send_get(self,url,data):
        result = requests.get(url=url,data=data).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':#如果是post，就发送post请求
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result
if __name__ == '__main__':
    result = RunMain().run_main('post','http://127.0.0.1:8888/login','name=xiaoming&pwd')
    print(result)
