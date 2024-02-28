# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest, time
from po.xj_kaoping.xj_gui_student.s_01 import S01
from common.yaml_util import YamlUtil

class TestXj014StuExam(object):

    s = S01(r'./pic/xj')       # 注意这里是从根目录下run得，所以传值需这样
    ya = YamlUtil()

    @pytest.mark.xj_smoke
    def test_stu_exam(self):
        '''学生考试'''
        self.s.pre_exam()






