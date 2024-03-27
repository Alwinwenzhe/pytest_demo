# -*- coding: utf-8 -*-
import time
import pyautogui
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil
from selenium.webdriver.common.by import By
from po.jnt.oa_and.gui_and import GuiAnd


class AndLogin(object):
    '''登录页面'''

    url = '/#/login'

    account = (By.ID, "account")
    pwd = (By.ID, "password")
    log_button = (By.CLASS_NAME, 'ant-btn.ant-btn-primary.ant-btn-lg.ant-btn-block')  # 登录按钮
    user_account = (By.CLASS_NAME, 'vben-header-user-dropdown__name.truncate')  # 账户
    exit_oa = (By.XPATH, '//*[@id="htmlRoot"]/body/div[8]/div/div/ul/li[3]/span/span/span[2]')  # 退出系统

    def __init__(self, driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()
        self.gui_and = GuiAnd()

    def log_in(self, user_name, password):
        '''登录操作'''
        self.web.open(self.ya.read_extract_yaml('and_oa_url') + self.url)
        self.web.send(*self.account, user_name)
        self.web.send(*self.pwd, password)
        self.web.click(*self.log_button)

    def log_out(self):
        '''
        退出登录
        :return:
        '''
        time.sleep(8)
        self.web.click(*self.user_account)
        time.sleep(3)
        # self.web.click(*self.exit_oa)
        self.gui_and.log_out()


if __name__ == '__main__':
    lo = AndLogin()
    lo.log_in('chenwenzhe', '123456')
