# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class XJ02LogExit(object):

    # 管理旁边的下拉按钮
    drop_down = (By.XPATH, '//span[contains(text(),"管理员")]/following-sibling::i')
    exi = (By.XPATH,'//span[text()="退出"]')

    def __init__(self,driver):
        self.web = WebKey(driver)

    def exit_login(self):
        '''
        退出登录操作
        :return:
        '''
        self.web.click(*self.drop_down)
        self.web.click(*self.exi)

