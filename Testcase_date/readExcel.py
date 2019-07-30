import os
from Testcase_date.getpathInfo import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
# 调用读Excel的第三方库xlrd
from xlrd import open_workbook

# 拿到该项目所在的绝对路径
path = getpathInfo().get_Path()
print(path)
class readExcel():
    def get_xls(self, zj, ww):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, "testFile", 'case', 'zj.xlsx')
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(ww)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls
if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    print(readExcel().get_xls('zj.xlsx', 'ww'))
    print(readExcel().get_xls('zj.xlsx', 'ww')[0][1])
    print(readExcel().get_xls('zj.xlsx', 'ww')[1][2])
