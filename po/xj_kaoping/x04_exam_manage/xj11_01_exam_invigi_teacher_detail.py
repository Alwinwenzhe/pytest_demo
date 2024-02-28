# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil


class Xj1101ExamInvigiTeacherDetail(object):
    '''考试计划详情___监考老师详情页面'''

    # id_card是动态值，使用starts-with
    # invigi_id_card = (By.CLASS_NAME,'//td[starts-with(@class,"el-table_23_column_")][2]/div')
    invigi_id_card = (By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[2]/div')
    # 学生姓名
    stu_name = (By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[1]/div')
    # 学校
    school_name = (By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[7]/div')
    # 考点
    exam_place = (By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[8]/div')

    # 退出
    user_avatar = (By.CLASS_NAME, 'avatar-wrapper.el-dropdown-selfdefine')
    log_out_ele = (By.XPATH, '//span[text()="退出"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def get_invigi_id_card(self):
        '''获取监考老师身份证号并写入配置中'''
        id_card =  self.web.find_ele(*self.invigi_id_card).text
        self.ya.write_inter_yaml('invigi_teacher_id',id_card)

    def get_school_name(self):
        '''获取学校名并写入配置中'''
        get_school_name = self.web.find_ele(*self.school_name).text
        self.ya.write_inter_yaml('school_name', get_school_name)

    def get_exam_place(self):
        '''获取考点名写入配置'''
        get_exam_name = self.web.find_ele(*self.exam_place).text
        self.ya.write_inter_yaml('exam_place', get_exam_name)

    def get_necessary_info(self):
        '''获取必要信息并写入配置'''
        self.get_invigi_id_card()
        self.get_school_name()
        self.get_exam_place()

    def log_out(self):
        '''退出登录'''
        self.web.click(*self.user_avatar)
        self.web.wait(2)
        self.web.click(*self.log_out_ele)