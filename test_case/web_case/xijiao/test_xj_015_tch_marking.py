# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest
from po.xj_kaoping.xj05_teacher_login.kw02_marking import KW02Marking
from po.xj_kaoping.x01_home.login import Login

class Test015TchMarking(object):

    # 等待学生做完试卷即可阅卷
    # @pytest.mark.xj_smoke
    def test_marking(self,open_browser):
        '''阅卷'''
        login = Login(open_browser)
        marker = KW02Marking(open_browser)
        login.log_in(marker.get_mark_id(),'123456')
