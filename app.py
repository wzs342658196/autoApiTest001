# 存放全局变量，静态变量，公有的初始化类
# api,data,script 核心部分
# 设计顺序：从外到内，从上往下 scripts-> api -> data
# 实现顺序：从内到外，从下王上 data -> api -> scripts


# tools, run_suite.py ,report 报告
# app.py,log,api,script 日志


import os
# 全局变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))