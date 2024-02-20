# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.deal_time import DealTime


class Xj05CreateExam04ChooseSchool(object):

    url = 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'
    # 选择参加此次考试计划得学校
    choose_sch = (By.CLASS_NAME,'siteBox')
    # 选择全部学校
    screen_school= (By.CLASS_NAME,'iconfont.icon.icon-a-244')
    # screen_school = (By.XPATH,'//span[contains(text(),"学校筛选"]')
    # 定位七中
    AT_7 = (By.XPATH,'//span[contains(text(),"梅州市学艺中学")]')
    # 确定
    enter_js = ("document.getElementsByClassName('el-button el-button--primary el-button--medium')[1].click()")
    # 保存并下一步信息上传
    save_next = (By.XPATH,'//span[contains(text()," 保存并下一步信息上传 ")]')


    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()

    def choose_school(self):
        '''进行学校选择'''
        choose_sch_ele = self.web.find_ele(*self.choose_sch)
        ActionChains(self.web.driver).move_to_element(choose_sch_ele).perform()
        self.web.wait(3)
        self.web.click(*self.screen_school)
        self.web.click(*self.AT_7)
        self.web.exec_js(self.enter_js)
        self.web.click(*self.save_next)



