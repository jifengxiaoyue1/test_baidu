#coding=utf-8
import unittest
#把 test_baidu 目录添加到 path 下，这里用的相对路径
import sys
sys.path.append('E:/pythonproject/baidu/test_baidu')
from test_baidu import*

#这里需要导入测试文件
import start_test_baiduchangewindow,start_test_baidusearch,start_test_forwardback
import HTMLTestRunner
import time

#用例文件列表
def caselist():
    alltestnames = [
        start_test_baiduchangewindow.TestBaiduregin,
        start_test_baidusearch.TestBaidusearch,
        start_test_forwardback.StartTestForwardback
        ]
    print "success read case list!!"
    return alltestnames

