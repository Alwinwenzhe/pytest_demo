# -*- coding:utf-8 -*-
# Status:
# Time:

from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By
from common.deal_time import DealTime


class XJ04_Create_Exam(object):
    '''第4个功能模块考试管理'''

    url = 'http://192.168.6.167:3000/teachEvaluation/#/aiQuestion/addAiQuestion?state=0'

    # 基本信息
    base_inf = (By.XPATH,'//*[@id="tab-infoSetting"]')
    exam_name = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[1]/div/div[1]/input')
    exam_date = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[2]/div/div/input')
    answer_time = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[3]/div/div/span[2]')
    exam_interval = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[4]/div/div/span[2]')
    enable_ai = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[5]/div/div[1]/span')
    subject = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[8]/div/div/label[1]/span[1]/span')
    morning_start = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[9]/div[1]/div/div/div/input')
    morning_end = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[9]/div[3]/div/div/div/input')
    afternoon_start = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[10]/div[1]/div/div/div/input')
    afternoon_end = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[10]/div[3]/div/div/div/input')

    # 监考设置
    proctor_set = (By.XPATH,'//*[@id="tab-moniterSetting"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()

    def create_exam(self):
        '''创建考试流程'''
        self.base_info()
        self.proctor_setting()


    def base_info(self):
        '创建基本信息--仅有算法考后评分'
        self.web.send(*self.exam_name,'AT'+ "_" + str(self.tim.get_current_timestamp()))
        self.web.send(*self.exam_date,self.tim.get_cur_date())
        self.web.wait(1)
        self.web.click(*self.base_inf)
        self.web.wait(1)
        for i in range(5):
            self.web.click(*self.answer_time)
            self.web.click(*self.exam_interval)
        self.web.click(*self.enable_ai)
        self.web.click(*self.subject)
        self.web.wait(1)
        self.base_info_choose_time()

    def base_info_choose_time(self):
        '''选择考试时间，如果是下午，那么上午随意选；反之一样'''
        if self.tim.morning_or_afternoon() == 'afternoon':
            self.web.send(*self.morning_start,'00:00')
            self.web.click(*self.base_inf)
            self.web.wait(1)
            self.web.send(*self.morning_end,'00:05')
            self.web.click(*self.base_inf)
            self.web.wait(1)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_start,self.tim.get_time_int(self.tim.get_cur_time_add()))
            self.web.wait(1)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_end,self.tim.get_time_int(self.tim.get_cur_time_add(20)))
            self.web.wait(1)
        else:
            self.web.send(*self.morning_start, self.tim.get_time_int(self.tim.get_cur_time_add()))
            self.web.click(*self.base_inf)
            self.web.wait(1)
            self.web.send(*self.morning_end, self.tim.get_time_int(self.tim.get_cur_time_add(20)))
            self.web.click(*self.base_inf)
            self.web.wait(1)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_start, '12:00')
            self.web.wait(1)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_end, '12:05')
            self.web.wait(1)

    def  proctor_setting(self):
        '''基本信息—监考设置'''
        self.web.click(*self.proctor_set)
        self.web.wait(10)