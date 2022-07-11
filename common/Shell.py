# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午2:54
# @Author  : WangJuan
# @File    : Shell.py

"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod       # 静态方法：未实例化/实例化后都可调用，是类的工具包；变量都不可使用;
    def invoke(cmd):    # 静态方法不包含self
        # 用subprocess 这个模块来产生子进程,并连接到子进程的标准输入/输出/错误中去，还可以得到子进程的返回值；stdout--文件对象；
        # stderr--文件描述符(整数)；shell--windows下，相当于添加“cmd.exe /c”
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
