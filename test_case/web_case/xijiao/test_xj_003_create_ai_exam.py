# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest,time
from po.xj_kaoping.xj04_create_exam import XJ04_Create_Exam
from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class TestXJ003CreateAiExam:


    @pytest.mark.xijiao
    def test_xj_001_create_exam(self,open_browser):
        exam = XJ04_Create_Exam(open_browser)
        exam.create_exam()
