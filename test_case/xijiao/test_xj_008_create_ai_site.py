# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj07_create_exam_06_site import Xj07CreateExam06Site
from selenium.webdriver.common.by import By

class TestXj008CreateAiSite(object):
    '''创建AI考试选择考点'''

    @pytest.mark.xj_smoke
    def test_cho_site(self,open_browser):
        exam = Xj07CreateExam06Site(open_browser)
        exam.choose_site()
        exam.web.find_ele(By.XPATH,'//span[contains(text(),"保存并下一步安排")]')


