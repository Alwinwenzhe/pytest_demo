# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj08_create_exam_07_check_student import Xj08CreateExam07CheckStudent
from selenium.webdriver.common.by import By

class TestXj009CreateAiCheckStu(object):

    @pytest.mark.xj_smoke
    def test_check_stud(self,open_browser):
        '''查看学生'''
        exam = Xj08CreateExam07CheckStudent(open_browser)
        exam.test_check_stu()
        assert exam.web.find_ele(By.XPATH,'//span[contains(text(),"保存并完成考试计划")]')