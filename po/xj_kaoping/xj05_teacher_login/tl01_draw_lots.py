# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil


class Tl01DrawLots(object):

    # 考务管理
    teacher_manager = (By.CLASS_NAME,'el-submenu__title')
    drawing = (By.XPATH,'//span[text()="抽签"]')
    check = (By.XPATH,'//span[text()="查看"]')
    click_draw = (By.XPATH,'//span[text()="抽签"]')
    # 退出
    user_avatar = (By.CLASS_NAME, 'avatar-wrapper.el-dropdown-selfdefine')
    log_out = (By.XPATH, '//span[text()="退出"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def drawing_lot(self):
        '''进行抽签'''
        self.web.click(*self.teacher_manager)
        self.web.click(*self.drawing)

        ex_name = self.ya.read_extract_yaml('ex_name')
        # 指定计划下得抽签按钮
        draw_button = (By.XPATH, '//div[text()=" %s "]/../../td[4]/div/div/a'.format(ex_name))
        self.web.click(*draw_button)
        self.web.click(*self.check)

    def log_out(self):
        '''退出登录'''
        self.web.click(*self.user_avatar)
        self.web.click(*self.log_out)
