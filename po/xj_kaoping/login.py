# -*- coding: utf-8 -*-
from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By


class Login(object):
    '''登录页面'''

    url = 'http://192.168.6.167:3000/teachEvaluation/#/login?redirect=%2Fteacher%2Finvigilator'

    account = (By.NAME,"userName")
    pwd = (By.NAME,"password")
    remmber_status = (By.XPATH,'//*[@id="app"]/div/form/label/span[2]')
    log_button = (By.XPATH,'//*[@id="app"]/div/form/button')

    def __init__(self):
        self.web = WebKey()
        self.dri = self.web.driver
        self.web.open(self.url)

    def log_in(self,user_name,password):
        '''登录操作'''
        self.web.refresh()
        self.web.send(*self.account,user_name)
        self.web.send(*self.pwd,password)
        self.web.click(*self.remmber_status)
        self.web.click(*self.log_button)
        self.web.wait(10)

if __name__ == '__main__':
    lo = Login()
    lo.log_in('admin','123456')