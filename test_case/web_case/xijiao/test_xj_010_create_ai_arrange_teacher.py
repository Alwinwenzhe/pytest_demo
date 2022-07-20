# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj09_create_exam_08_arrange_teacher import Xj09CreateExam08ArrangeTeacher
from selenium.webdriver.common.by import By

class TestXj009CreateAiArrangeTeacher(object):

    @pytest.mark.xijiao
    def test_check_stud(self,open_browser):
        '''查看学生'''
        exam = Xj09CreateExam08ArrangeTeacher(open_browser)
        exam.arrange_teacher()
        exam.web.wait(20)