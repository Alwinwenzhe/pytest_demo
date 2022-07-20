# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest
from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class Xj08CreateExam07CheckStudent(object):

    url = 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 保存并下一步安排考务老师
    next = (By.XPATH,'//span[contains(text(),"保存并下一步安排考务老师")]')

    def __init__(self,driver):
        self.web = WebKey(driver)

    @pytest.mark.xijiao
    def test_check_stu(self):
        '''查看考生，这里并没有做任何校验操作'''
        self.web.click(*self.next)

