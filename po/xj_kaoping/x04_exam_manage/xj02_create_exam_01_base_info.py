# -*- coding:utf-8 -*-
# Status:
# Time:

from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By
from common.deal_time import DealTime
from common.yaml_util import YamlUtil


class XJ02_Create_Exam_01_Base_Info(object):
    '''第4个功能模块考试管理'''

    url = 'http://192.168.6.167:3000/teachEvaluation/#/aiQuestion/addAiQuestion?state=0'

    # 基本信息
    base_inf = (By.ID,'tab-infoSetting')
    exam_name = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[1]/div/div[1]/input')
    exam_date = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[2]/div/div/input')
    #   考试时间减
    answer_time = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[3]/div/div/span[1]')
    exam_interval = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[4]/div/div/span[1]')
    enable_ai = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[5]/div/div[1]/span')
    subject = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[8]/div/div/label[1]/span[1]/span')
    morning_start = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[9]/div[1]/div/div/div/input')
    morning_end = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[9]/div[3]/div/div/div/input')
    afternoon_start = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[10]/div[1]/div/div/div/input')
    afternoon_end = (By.XPATH,'//*[@id="pane-infoSetting"]/div/form/div[10]/div[3]/div/div/div/input')

    # 监考设置
    proctor_set = (By.ID,'tab-moniterSetting')
    # 监考老师人数
    invigilation_text = (By.XPATH,'//*[@id="pane-moniterSetting"]/div/form/div[3]/div/div/div/input')
    # 阅卷次数
    marking_text = (By.XPATH,'//input[@placeholder="请填写阅卷次数"]')

    # 考题分布设置
    distribution_of_exam = (By.ID,'tab-spreadSetting')
    distrbution_of_random = (By.XPATH,'//*[@id="pane-spreadSetting"]/div/form/div[1]/div/div/span')
    diffent_of_exam = (By.XPATH,'//*[@id="pane-spreadSetting"]/div/form/div[2]/div/div/span')

    # 其它设置
    other_settings = (By.ID,'tab-otherSetting')
    notice = (By.XPATH,'//*[@id="tinymce"]/p')
    save_buttion = (By.CLASS_NAME,'el-button.el-button--primary.el-button--medium')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()
        self.ya = YamlUtil()
        self.ex_name = 'AT' + "_" + self.tim.get_cur_date() + "_" + str(self.tim.get_current_timestamp()) + "_cwz"
        self.ya.write_inter_yaml('ex_name',self.ex_name)

    def create_exam(self):
        '''创建考试流程'''
        self.base_info()
        self.proctor_setting()
        self.dis_of_exam()
        self.other_set()

    def base_info(self):
        '创建基本信息--仅有算法考后评分'

        self.web.send(*self.exam_name,self.ex_name)

        # 移除只读属性
        self.web.exec_js("document.getElementsByClassName('el-input__inner')[3].removeAttribute('readonly')")
        self.web.send(*self.exam_date,self.tim.get_cur_date())
        self.web.click(*self.base_inf)
        for i in range(3):
            self.web.click(*self.answer_time)
        for i in range(2):
            self.web.click(*self.exam_interval)
        self.web.click(*self.enable_ai)
        # AI中得内容未操作
        self.web.click(*self.subject)
        self.base_info_choose_time()

    def base_info_choose_time(self):
        '''选择考试时间，如果是下午，那么上午随意选；反之一样'''
        # 先去除只读
        for i in range(6, 10):
            self.web.exec_js("document.getElementsByClassName('el-input__inner')[{0}].removeAttribute('readonly')".format(i))
        start_time = self.tim.get_cur_time_add_and_write()
        if self.tim.morning_or_afternoon(start_time) == 'afternoon':
            self.web.send(*self.morning_start,'00:00')
            self.web.click(*self.base_inf)
            self.web.send(*self.morning_end,'00:05')
            self.web.click(*self.base_inf)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_start,start_time)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_end,self.tim.get_time_int(self.tim.get_cur_time_add(60)))
        else:
            self.web.send(*self.morning_start, start_time)
            self.web.click(*self.base_inf)
            self.web.send(*self.morning_end, self.tim.get_time_int(self.tim.get_cur_time_add(60)))
            self.web.click(*self.base_inf)
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_start, '12:00')
            self.web.click(*self.base_inf)
            self.web.send(*self.afternoon_end, '12:05')
        self.ya.write_inter_yaml('exam_start_time',start_time)


    def proctor_setting(self):
        '''基本信息—监考设置'''
        self.web.click(*self.proctor_set)
        # 将监考老师和阅卷次数设置为1
        self.web.send(*self.invigilation_text,self.ya.read_extract_yaml('invigilation_num'))
        self.web.send(*self.marking_text,self.ya.read_extract_yaml('marking_num'))

    def dis_of_exam(self):
        '''考题分布，'''
        self.web.click(*self.distribution_of_exam)
        self.web.click(*self.distrbution_of_random)
        self.web.click(*self.diffent_of_exam)

    def other_set(self):
        '''其它设置'''
        self.web.click(*self.other_settings)
        self.web.switch_frame(By.ID,'tinymce_ifr')
        self.web.send(*self.notice,'AT_这是自动化生成得公告内容，用以区分普通计划')
        self.web.switch_default()
        self.web.click(*self.save_buttion)


