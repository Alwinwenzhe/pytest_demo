# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest
from po.xj_kaoping.x04_exam_manage.xj10_exam_list import Xj10ExamListCreateSession
from po.xj_kaoping.x04_exam_manage.xj11_00_exam_list_exam_detail import Xj1100ExamListExamDetail
from selenium.webdriver.common.by import By

class TestXj011ExamRelease(object):

    @pytest.mark.xj_smoke
    def test_audit_exam(self,open_browser):
        '''发布考试'''
        exam_list = Xj10ExamListCreateSession(open_browser)
        exam_detail = Xj1100ExamListExamDetail(open_browser)

        exam_list.check_exam()
        exam_detail.create_sess()
        exam_list.audit_exam()
        assert exam_list.web.find_eles(By.XPATH,'//span[text()="查看"]')