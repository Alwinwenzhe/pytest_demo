# -*- coding:utf-8 -*-
# Status:
# Time:

from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By
from common.deal_time import DealTime


class XJ03_Create_Exam_02_Subject(object):

    url= 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'


    #从题库选择
    sub_library = (By.CLASS_NAME,'iconfont.build.icon-a-24-3333333')
    #   题目搜索
    subject_title = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div/div/div/input')
    #   查询按钮
    search = (By.XPATH,'//span[text()="查询"]')
    #   选择全部
    choose_all = (By.XPATH,'//span[text()=" 选择全部 "]')
    #   确定 有两种方式
    # enter = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div[2]/div/div[3]/div[3]/div/div/div[3]/span/button[2]/span')
    enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[2].click()"

    #   保存并下一步选择区县
    next = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div[2]/div/div[4]/button/span')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()

    def choose_subject(self):
        '''选择自己创建得对应科目全部考题'''
        self.web.click(*self.sub_library)
        self.web.send(*self.subject_title,'质量')
        self.web.click(*self.search)
        self.web.click(*self.choose_all)
        self.web.exec_js(self.enter_js)
        self.web.click(*self.next)



