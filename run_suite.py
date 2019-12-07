# 执行测试套件的入口
import unittest

import os

import time

from script.TestLogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
import app
# 初始化测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
# 初始化测试报告的路径和名称
report_path = app.BASE_DIR+"/report/tpshop{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,mode="wb")as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f,verbosity=1,description="tpshop的测试报告",title="Tpshop")
    # 使用runner运行测试套件
    runner.run(suite)