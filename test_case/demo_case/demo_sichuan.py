# -*- coding:utf-8 -*-
# Status:主动刷新页面，直到成功后，进行语音播报，等待输入
# Time:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.voice import Voice

if __name__ == '__main__':
    voice = Voice()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://zk.sceea.cn/")

    for i in range(100):
        if driver.title == "":
            time.sleep(10)
        elif driver.title == "四川省考试院-高等教育自学考试管理信息系统报考端":
            time.sleep(3)
            for i in range(3):
                voice.machine_read("成功进入四川省考试院，等输入考生信息")
                input("yonghushuru ")
