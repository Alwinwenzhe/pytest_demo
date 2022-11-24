# -*- coding:utf-8 -*-
# Status:  选择高新东区还有问题
# Time:
from common.web_common.web_key import WebKey
from common.deal_time import DealTime
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Xj04CreateExam03County(object):

    url = 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 区县框
    county_area = (By.XPATH,'//div[@class="siteChoose"]/div[2]/div')
    # 移除区县得隐藏属性
    remove_display = "document.getElementsByClassName('mask')[0].removeAttribute('style')"
    # 筛选区县
    screening_county = (By.XPATH,'//span[text()="区县筛选"]')

    # screening_county_js_click = "document.elementFromPoint(1100,660).click()"
    # 直接定位；更准确得是通过名字定位AT_高新东区_cwz，找兄弟
    east_area = (By.XPATH,'//span[contains(text(),"AT_高新东区_cwz")]')
    # 确定
    enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[1].click()"
    # 保存并下一步
    next = (By.XPATH,'//span[contains(text(),"下一步选择学校")]')


    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()

    def choose_county(self):
        '''选择区县'''
        # 移动鼠标 显示区县选择区域
        self.web.wait(3)
        self.web.exec_js(self.remove_display)
        # find_county_ele = self.web.find_ele(*self.county_area,timeout=30)
        # ActionChains(self.web.driver).move_to_element(find_county_ele).perform()
        self.web.click(*self.screening_county)
        self.web.click(*self.east_area)
        self.web.wait(1)
        self.web.exec_js(self.enter_js)
        self.web.click(*self.next)




