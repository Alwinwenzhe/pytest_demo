# -*- coding: utf-8 -*-
from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By
from common.yaml_util import YamlUtil


class Login(object):
    '''登录页面'''

    url = '/teachEvaluation/#/login?redirect=%2Fteacher%2Finvigilator'

    account = (By.NAME,"userName")
    pwd = (By.NAME,"password")
    remmber_status = (By.XPATH,'//*[@id="app"]/div/form/label/span[2]')
    log_button = (By.XPATH,'//*[@id="app"]/div/form/button')

    # 选择组织机构弹窗
    organize = (By.CLASS_NAME,'el-dialog.el-dialog--center')
    # 请选择组织机构
    choose_orga = (By.CLASS_NAME,'el-input.el-input--medium.el-input--suffix')
    organize_list = (By.XPATH,'//ul/li/span')
    enter = (By.CLASS_NAME,'el-button.el-button--primary.el-button--medium')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def log_in(self,user_name,password):
        '''登录操作'''
        self.web.open(self.ya.read_extract_yaml('ip') + self.url)
        self.web.send(*self.account, user_name)
        self.web.send(*self.pwd, password)
        self.web.click(*self.remmber_status)
        self.web.click(*self.log_button)
        if len(user_name) > 13:
            self.web.wait(4)
            self.choose_org()

    def choose_org(self):
        '''选择组织机构'''
        self.web.move_to_ele_and_click(self.web.driver,self.choose_orga,self.choose_orga)
        sch_name = self.ya.read_extract_yaml('school_name')
        eles = self.web.find_eles(*self.organize_list)
        for i in eles:
            self.web.wait(1)
            if i.text == sch_name:
                i.click()

        self.web.click(*self.enter)


if __name__ == '__main__':
    lo = Login()
    lo.log_in('admin','123456')