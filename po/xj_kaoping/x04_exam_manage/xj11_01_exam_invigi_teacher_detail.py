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

    # 退出
    user_avatar = (By.CLASS_NAME, 'avatar-wrapper.el-dropdown-selfdefine')
    log_out_ele = (By.XPATH, '//span[text()="退出"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def get_invigi_id_card(self):
        '''获取监考老师身份证号并写入根目录yaml中'''
        id_card =  self.web.find_ele(*self.invigi_id_card).text
        self.ya.write_inter_yaml('invigi_teacher_id',id_card)

    def log_out(self):
        '''退出登录'''
        self.web.click(*self.user_avatar)
        self.web.wait(2)
        self.web.click(*self.log_out_ele)