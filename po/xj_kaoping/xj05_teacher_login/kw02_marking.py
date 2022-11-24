# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil
from po.xj_kaoping.x01_home.xj02_log_exit import XJ02LogExit
from common.deal_time import DealTime

class KW02Marking(object):


    # 考务管理
    teacher_manager = (By.CLASS_NAME, 'el-submenu__title')
    # 阅卷菜单
    mark_menu = (By.XPATH,'//span[text()="阅卷详情"]')
    # 待阅数量
    mark_num = (By.XPATH,'//i[@class="el-icon-s-order"]/..')
    # 下一卷
    next_paper = (By.XPATH,'//span[text()=" 下一卷 "]')
    # 满分
    score_100 = (By.XPATH,'//span[text()="满分"]')
    score_0 = (By.XPATH,'//span[text()="零分"]')
    # 确认并提交
    submit = (By.XPATH,'//span[text()=" 确认成绩并提交 "]')
    # 确认提示框
    confirm_ok = (By.XPATH,'//span[text()="确定"]')


    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()
        self.ex = XJ02LogExit

    def get_mark_id(self):
        '''获取阅卷老师id'''
        return self.ya.read_extract_yaml('marking_id')

    def enter_marking(self):
        '''进入阅卷'''
        self.web.click(*self.teacher_manager)
        self.web.click(*self.mark_menu)
        self.web.wait(1)
        # 阅卷按钮
        mark_button = (By.XPATH, '//div[text()=" {0} "]/../../td[5]/div/div/a'.format(self.ya.read_extract_yaml('exam_name')))
        self.web.click(*mark_button)

    def vedio_play(self):
        '''视频播放验证'''
        pass

    def next_test_paper(self):
        '''下一卷'''
        self.web.click(*self.next_paper)
        self.web.is_toast_exist('获取下一卷成功！')

    def mark_score(self):
        '''阅卷打分'''
        self.next_test_paper()
        # 打分，前面都满分，最后一个零分
        score_full = self.web.find_eles(*self.score_100)
        score_empty = self.web.find_eles(*self.score_0)
        for k,v in enumerate(score_full):
            if len(score_full)-1 != k:
                v.click()
            else:
                for i in score_empty[-1::]:
                    i.click()

    def enter_submit(self):
        '''确认并提交成绩'''
        self.web.click(*self.submit)
        self.web.click(*self.confirm_ok)
        self.web.is_toast_exist('考卷评分成功！')

    def get_mark_num(self):
        '''获取阅卷数量'''
        return (self.web.find_ele(*self.mark_num).text).split(" ")[1]

    def log_out(self):
        '''退出登录'''
        self.ex.exit_login()

    def mark_main(self):
        '''阅卷入口'''
        self.enter_marking()
        while self.get_mark_num() > 1:
            self.next_test_paper()
            break
        while self.get_mark_num() > 0:
            self.mark_score()
            self.enter_submit()
        self.log_out()










