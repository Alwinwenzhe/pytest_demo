# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil
from common.deal_time import DealTime


class KW01DrawLots(object):

    # 考务管理
    teacher_manager = (By.CLASS_NAME,'el-submenu__title')
    drawing = (By.XPATH,'//span[text()="抽签"]')

    # 抽签按钮
    click_draw = (By.CLASS_NAME, 'el-button.reset.el-button--primary.el-button--medium')
    draw_button2 = (By.CLASS_NAME,'el-link.el-link--primary.is-underline')
    # 退出
    user_avatar = (By.CLASS_NAME, 'avatar-wrapper.el-dropdown-selfdefine')
    log_ou = (By.XPATH, '//span[text()="退出"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()
        self.dl = DealTime()

    def drawing_lot(self):
        '''进行抽签,并退出'''
        # 抽签菜单
        self.web.click(*self.teacher_manager)
        self.web.click(*self.drawing)

        ex_name = self.ya.read_extract_yaml('ex_name')
        #等待到特定时间进入
        start_time = self.ya.read_extract_yaml('start_time_stamp')
        self.dl.wait_until_start(start_time)
        self.web.refresh()
        # 指定计划下得抽签按钮
        draw_button = (By.XPATH, '//div[text()=" {0} "]/../../td[4]/div/div/a'.format(ex_name))
        self.web.click(*draw_button)
        self.web.wait(1)
        self.web.click(*self.draw_button2)
        self.web.wait(1)
        self.web.click(*self.click_draw)

    def log_out(self):
        '''退出登录'''
        self.web.click(*self.user_avatar)
        self.web.click(*self.log_ou)
