# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey


class XJ02LogExit(object):
    # 管理旁边的下拉按钮
    # 退出
    user_avatar = (By.CLASS_NAME, 'avatar-wrapper.el-dropdown-selfdefine')
    log_out = (By.CLASS_NAME, '//span[text()="退出"]')

    def __init__(self, driver):
        self.web = WebKey(driver)

    def exit_login(self):
        '''
        退出登录操作
        :return:
        '''
        self.web.click(*self.user_avatar)
        self.web.click(*self.exi)
