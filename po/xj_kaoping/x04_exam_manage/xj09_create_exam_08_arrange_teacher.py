# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class Xj09CreateExam08ArrangeTeacher(object):

    url ='http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 安排监考老师
    invigilation_area = (By.CLASS_NAME,'siteBox')
    # 选择姓名
    name_tab = (By.XPATH,'//span[@class="el-radio-button__inner"]')
    # 监考checkbox
    invit_teachers = (By.CLASS_NAME,'el-table_20_column_126.is-center.el-table-column--selection')
    # 组长自动分配
    auto = (By.XPATH,'//div[@class="leader"]/div[1]')
    # 确定
    enter_js = 'document.getElementsByClassName("el-button el-button--primary el-button--medium")[4]'

    # 安排阅卷老师
    marking_teacher = (By.ID,'tab-reviewTeacher')


    def __init__(self,driver):
        self.web = WebKey(driver)

    def arrange_teacher(self):
        '''安排考务老师'''
        self.arrange_invigilation()
        self.arrrange_marking()

    def arrange_invigilation(self):
        '''安排监考老师',默认一个考点2个老师，使用自动分配组长'''
        self.web.click(*self.invigilation_area)
        self.web.click(self.web.find_eles(*self.name_tab)[3])
        self.two_invigi()
        self.web.click(*self.auto)
        self.web.exec_js(self.enter_js)

    def arrrange_marking(self):
        self.web.click(*self.marking_teacher)

    def two_invigi(self):
        '''选择2个监考老师'''
        j = 1
        for i in self.invit_teachers:
            self.web.click(i)
            j +=1
            if j >=2:
                break

