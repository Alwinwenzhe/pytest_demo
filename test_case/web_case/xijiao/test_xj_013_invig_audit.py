# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.xj_gui_teacher.tc_01 import TC01

class TestXj001InvigAudit(object):

    tc = TC01(r'./pic/xj')

    @pytest.mark.gui
    @pytest.mark.xj_smoke
    def test_invig_audit(self):
        '''监考老师审核'''
        self.tc.teache_audit()
        print('run success!!')