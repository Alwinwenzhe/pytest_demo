# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil


class Xj10ExamListCreateSession(object):

    exam_list = 'http://192.168.6.167:3000/teachEvaluation/#/plan/list'
    # 搜索
    input_exam_name = (By.XPATH,'//input[@placeholder="请输入考试名称"]')
    query_button =  (By.XPATH,'//span[text()="查询"]')

    # 列表信息
    check = (By.XPATH,'//span[text()="查看"]')
    start_audit = (By.XPATH,'//span[text()="发起审核"]')
    audit = (By.XPATH,'//span[text()="审核"]')
    publish = (By.XPATH,'//span[text()="发布"]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()
        self.ex_name = self.ya.read_extract_yaml('ex_name')

    def search_exam(self):
        '''搜索考试名'''
        self.web.send(*self.input_exam_name,self.ex_name)
        self.web.click(*self.query_button)

    def check_exam(self):
        '''搜索并点击查看'''
        self.search_exam()
        self.web.wait(1)
        self.web.click(*self.check)

    def audit_exam(self):
        '''发起审核、审核、发布'''
        self.search_exam()
        self.web.click(*self.start_audit)
        self.web.click(*self.audit)
        self.web.click(*self.publish)
        self.web.refresh()


