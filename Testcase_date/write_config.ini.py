# -*- coding: utf-8 -*-
import configparser
config=configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')#读取“config.in”文件，没有则创建“config.in”文件
"""config.add_section('HTTP') #添加为“HTTP”的section
config.set('HTTP','scheme','http')#为section添加属性
config.set('HTTP','baseurl','127.0.0.1')
config.set('HTTP','port','8888')
config.set('HTTP','timeout','10.0')"""
config.add_section('EMAIL')
#config.set('EMAIL','on_off','on;')
#config.set('EMAIL','subject','周周接口自动化测试报告')
#config.set('EMAIL','app','Outlook')
config.set('EMAIL','username','jol@163.com')
config.set('EMAIL','recv','zhoujun@163.net')
config.write(open('config.ini','w'))#写入文件
