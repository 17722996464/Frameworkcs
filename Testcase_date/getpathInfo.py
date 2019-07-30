import os
class getpathInfo():

    def get_Path(path):
        path = os.path.split(os.path.realpath(__file__))[0]
        #os.path.realpath(path)  #返回path的真实路径
        #os.path.split(path)  #把路径分割成dirname和basename，返回一个元组
        #os.path.dirname(path) #返回文件路径
        # os.path.basename(path) #返回文件名
        #xlsPath = os.path.join(path, "testFile", 'case', 'zj.xlsx')
        return path
if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', getpathInfo().get_Path())
