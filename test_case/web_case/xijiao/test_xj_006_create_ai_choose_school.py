# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj05_create_exam_04_choose_school import Xj05CreateExam04ChooseSchool
from selenium.webdriver.common.by import By

class TestXj006CreateAiChooseSchool(object):

    @pytest.mark.xj_smoke
    def test_01_choose_school(self,open_browser):
        choose_sch = Xj05CreateExam04ChooseSchool(open_browser)
        choose_sch.choose_school()
        assert choose_sch.web.find_ele(By.XPATH,'//span[contains(text(),"保存并开始下一步选择考点")]')
        choose_sch.web.wait(10)
