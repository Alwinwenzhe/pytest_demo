# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj03_create_exzm_02_subject import XJ03_Create_Exam_02_Subject
from selenium.webdriver.common.by import By

class TestXJ004CreateAiExamChooseSubject(object):

    @pytest.mark.xijiao
    def test_01_create_exam_choose_sub(self,open_browser):
        exam = XJ03_Create_Exam_02_Subject(open_browser)
        exam.choose_subject()
        assert exam.web.find_ele(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[2]/div/div[4]/button[1]/span')
