# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj02_create_exam_01_base_info import XJ02_Create_Exam_01_Base_Info
from selenium.webdriver.common.by import By

class TestXJ003CreateAiExamBaseInfo:

    @pytest.mark.xijiao
    def test_01_create_exam_base(self,open_browser):
        exam = XJ02_Create_Exam_01_Base_Info(open_browser)
        exam.create_exam()
        assert exam.web.find_ele(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[2]/div/div[4]/button/span')
