# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest,time
from po.xj_kaoping.exam_manage import Exam_Manage
from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey

class TestXJ002ExamManage:


    @pytest.mark.xijiao
    def test_xj_002_create_exam(self,open_browser):
        exam = Exam_Manage(open_browser)
        exam.create_exam_po()
        assert 1==1;