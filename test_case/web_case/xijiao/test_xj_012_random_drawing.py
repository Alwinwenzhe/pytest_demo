# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj11_00_exam_list_exam_detail import Xj1100ExamListExamDetail
from po.xj_kaoping.x04_exam_manage.xj11_01_exam_invigi_teacher_detail import Xj1101ExamInvigiTeacherDetail
from po.xj_kaoping.x04_exam_manage.xj10_exam_list import Xj10ExamListCreateSession
from po.xj_kaoping.x01_home.login import Login
from common.yaml_util import YamlUtil
from selenium.webdriver.common.by import By

class TestXj012RandomDrawing(object):

    ya = YamlUtil()
    pwd = '123456'

    @pytest.mark.xj_smoke
    def test_random_drawing(self,open_browser):
        '''获取监考老师身份证号码，并登录抽签'''
        xjee = Xj1100ExamListExamDetail(open_browser)
        xj_invi = Xj1101ExamInvigiTeacherDetail(open_browser)
        xj_login = Login(open_browser)
        xj_exam_list = Xj10ExamListCreateSession(open_browser)

        # 查询并进入详情
        xj_exam_list.check_exam()

        # 获取监考老师身份证号码，并退出
        xjee.enter_invigilation_teachers()
        xj_invi.get_invigi_id_card()
        xj_invi.log_out()

        # 登录、选机构、并抽签
        invi_account = self.ya.read_extract_yaml('invigi_teacher_id')
        xj_login.log_in(invi_account,self.pwd)


