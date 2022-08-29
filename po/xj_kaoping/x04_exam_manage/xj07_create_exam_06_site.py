# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from selenium.webdriver.common.action_chains import ActionChains

class Xj07CreateExam06Site(object):

    url = 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 考点区域
    site_area = (By.CLASS_NAME,'siteBox')
    # 考点筛选
    screen_site = (By.XPATH,'//span[text()="考点筛选"]')
    # 选择考点
    choo_site = (By.XPATH,'//span[text()="AT_成都七中_东区总校_cwz"]')
    # 确定
    enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[1].click()"
    # 保存并下一步查看考生
    next = (By.XPATH,'//span[contains(text(),"保存并下一步查看考生")]')

    def __init__(self,driver):
        self.web = WebKey(driver)

    def choose_site(self):
        '''选择考点'''
        ActionChains(self.web.driver).move_to_element(self.web.find_ele(*self.site_area)).perform()
        self.web.click(*self.screen_site)
        self.web.click(*self.choo_site)
        self.web.exec_js(self.enter_js)
        self.web.click(*self.next)

