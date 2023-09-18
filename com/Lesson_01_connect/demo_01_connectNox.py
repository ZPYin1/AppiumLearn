# -*- coding: utf-8 -*-
'''
@Time    : 2023/5/18 16:09
@Author  : Silver
@File    : demo_01_connectNox.py

'''
# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-6-17
@author: 北京-宏哥   QQ交流群：707699217
Project:学习和使用python代码appium+pycharm+连接夜神模拟器
'''
# 3.导入模块
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'   #android的apk还是IOS的ipa
desired_caps['platformVersion'] = '5.1.1'  #android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62025'    #手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.taobao.taobao'  #apk的包名
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'  #apk的launcherActivity
# desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard'] = True     # # 将键盘给隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  ##启动服务器地址，后面跟的是手机