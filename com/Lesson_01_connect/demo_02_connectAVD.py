# -*- coding: utf-8 -*-
'''
@Time    : 2023/5/18 16:28
@Author  : Silver
@File    : demo_02_connectAVD.py

'''
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'   #android的apk还是IOS的ipa
desired_caps['platformVersion'] = '13.0'  #android系统的版本号
desired_caps['deviceName'] = 'emulator-5554'    #手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.taobao.taobao'  #apk的包名
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'  #apk的launcherActivity
# desired_caps['unicodeKeyboard'] = True   #使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard'] = True   #将键盘给隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #启动服务器地址，后面跟的是手机信息