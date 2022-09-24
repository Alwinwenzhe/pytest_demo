# -*- coding:utf-8 -*-
# Status:
# Time:

from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By


class XJ01_Exam_Manage(object):
    '''第4个功能模块考试管理'''

    url_home = 'http://192.168.6.167:3000/teachEvaluation/#/dashboard'


    # 考试管理
    exam_management = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div')
    # 考试管理--考试列表
    exam_list = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li')
    # 考试管理--考试列表--创建考试
    create_exam = (By.XPATH,'//button[@class="el-button addSite el-button--primary el-button--medium"]/span/i')

    def __init__(self,driver):
        self.web = WebKey(driver)

    def create_exam_po(self):
        '''登录操作'''
        self.web.open(self.url_home)
        self.web.click(*self.exam_management)
        self.web.click(*self.exam_list)
        self.web.click(*self.create_exam)
        self.web.wait(1)

