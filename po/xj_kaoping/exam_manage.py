# -*- coding:utf-8 -*-
# Status:
# Time:

from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By


class Exam_Manage(object):
    '''登录页面'''

    url_home = 'http://192.168.6.167:3000/teachEvaluation/#/dashboard'


    # 考试管理
    exam_management = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div')
    # 考试管理--考试列表
    exam_list = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li')
    # 考试管理--考试列表--创建考试
    create_exam = (By.CLASS_NAME,'el-icon-circle-plus-outline')

    def __init__(self,driver):
        self.web = WebKey(driver)

    def create_exam_po(self):
        '''登录操作'''
        self.web.open(self.url_home)
        self.web.click(*self.exam_management)
        self.web.wait(10)

