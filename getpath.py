import os
class getpathInfo():

    def get_Path(path):
        path = os.path.split(os.path.realpath(__file__))[0]
        #xlsPath = os.path.join(path, "testFile", 'case', 'zj.xlsx')
        return path
if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', getpathInfo().get_Path())
