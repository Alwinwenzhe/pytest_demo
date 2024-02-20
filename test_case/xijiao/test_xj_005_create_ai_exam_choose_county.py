# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj04_create_exam_03_county import Xj04CreateExam03County
from selenium.webdriver.common.by import By

class TestXj005CreateAiExamChooseCouty(object):

    @pytest.mark.xj_smoke
    def test_01_choose_couty(self,open_browser):
        '''选择区县'''
        exam = Xj04CreateExam03County(open_browser)

        exam.choose_county()
        assert exam.web.find_ele(By.XPATH,"//span[contains(text(),'下一步信息上传')]")
        exam.web.wait(20)