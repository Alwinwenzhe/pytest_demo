# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest,time
from po.xj_kaoping.xj04_exam_manage import XJ04_Exam_Manage
from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class TestXJ002ExamManage:


    @pytest.mark.xijiao
    def test_xj_002_enter_exam(self,open_browser):
        exam = XJ04_Exam_Manage(open_browser)
        exam.create_exam_po()
        assert exam.web.assert_url('http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd')
