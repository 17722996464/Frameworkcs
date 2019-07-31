from Testcase_date.readConfig import ReadConfig
readConfig = ReadConfig()
class geturlParmes():
    def get_url(self):     #定义一个方法，读取配置文件进行拼接
        new_url= readConfig.get_http('scheme') + '://'+readConfig.get_http('baseurl')+':8888'+'/login'+'?'
        return new_url
if __name__ == '__main__':
    print(geturlParmes().get_url())