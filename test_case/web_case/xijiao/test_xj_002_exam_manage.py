# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj01_exam_manage import XJ01_Exam_Manage

class TestXJ002ExamManage:


    @pytest.mark.xj_smoke
    def test_xj_002_enter_exam(self,open_browser):
        exam = XJ01_Exam_Manage(open_browser)
        exam.create_exam_po()
        assert exam.web.assert_url('http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd')
