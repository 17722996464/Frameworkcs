# -*- coding: utf-8 -*-
import configparser
config=configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')
config.set('EMAIL','username','jol@163.com')
config.set('EMAIL','recv','zhoujun@163.net')
config.set('EMAIL','passwd','zj123456')
config.set('EMAIL','content','20190723测试报告结果')
config.set('EMAIL','title','自动化测试报告')
config.write(open('config.ini','w'))
