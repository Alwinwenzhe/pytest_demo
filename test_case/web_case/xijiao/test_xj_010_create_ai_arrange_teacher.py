# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj09_create_exam_08_arrange_teacher import Xj09CreateExam08ArrangeTeacher
from selenium.webdriver.common.by import By

class TestXj010CreateAiArrangeTeacher(object):

    @pytest.mark.xj_smoke
    def test_arrange_teacher(self,open_browser):
        '''查看学生'''
        exam = Xj09CreateExam08ArrangeTeacher(open_browser)
        exam.arrange_teacher()
        exam.web.wait(20)
        assert exam.web.find_ele(By.XPATH, '//span[text()="创建考试"]')