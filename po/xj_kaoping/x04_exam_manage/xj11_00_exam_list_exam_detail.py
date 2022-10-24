# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from po.xj_kaoping.x04_exam_manage.xj02_create_exam_01_base_info import XJ02_Create_Exam_01_Base_Info as x02


class Xj1100ExamListExamDetail(object):

    # 生成场次
    create_session = (By.XPATH,'//span[text()=" 生成场次 "]/..')
    retur = (By.XPATH,'//span[text()="返回"]')

    # 监考老师模块
    invigilation_teachers = (By.XPATH,'//span[text()=" 监考老师 "]')
    # 查看学校
    check_school = (By.XPATH,'//span[text()=" 查看学校 "]')

    def __init__(self,driver):
        self.web = WebKey(driver)

    def create_sess(self):
        '''生成场次'''
        self.web.click(*self.create_session)
        self.web.wait(2)
        self.web.click(*self.retur)

    def enter_invigilation_teachers(self):
        '''进入监考老师模块'''
        self.web.click(*self.invigilation_teachers)

    def enter_check_school(self):
        '''进入查看学校'''
        self.web.click(*self.check_school)







