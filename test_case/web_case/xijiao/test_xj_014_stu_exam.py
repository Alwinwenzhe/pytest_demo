# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest, time
from po.xj_kaoping.xj_gui_student.s_01 import S01
from common.yaml_util import YamlUtil

class TestXj014StuExam(object):

    s = S01(r'./pic/xj/stu/')       # 注意这里是从根目录下run得，所以传值需这样
    ya = YamlUtil()

    @pytest.mark.gui_demo
    @pytest.mark.xj_smoke
    def test_stu_exam(self):
        '''学生考试'''
        # 启动并设置校级服务器
        self.s.routine('001_pc_home.jpg','001_pc_home_stu_client.png',click='d',name='001_pc_home_stu_client.png')
        time.sleep(3)
        self.s.routine('002_stu_home.jpg','002_stu_home_set.jpg',name='002_stu_home_set.jpg')
        self.s.routine('002_stu_home_oper.jpg','002_stu_home_oper_pwd.jpg',name='002_stu_home_oper_pwd.jpg')
        self.s.input_con('123456')
        self.s.routine('002_stu_home_oper.jpg', '002_stu_home_oper_enter.jpg',name='002_stu_home_oper_enter.jpg')
        time.sleep(2)
        # 修改校级服务器地址
        self.s.routine('003_stu_base_set.jpg','003_stu_base_set_sch_server.jpg',name='003_stu_base_set_sch_server.jpg')
        self.s.clear_and_input_con(self.s.get_server_ip())
        # 修改考点
        self.s.routine('003_stu_base_set.jpg','003_stu_base_set_exam_place.jpg',add_x=200,name='003_stu_base_set_exam_place.jpg')
        self.s.routine('003_stu_base_set_exam_place.jpg','003_stu_base_set_exam_place_search.jpg',name='003_stu_base_set_exam_place_search.jpg')
        self.s.input_con(self.s.get_exam_place())
        self.s.routine('003_stu_base_set_exam_place.jpg','003_stu_base_set_exam_place_sch_g.jpg',add_y=100,name='003_stu_base_set_exam_place_sch_g.jpg')
        # 默认物理考场
        # 座位号
        self.s.routine('003_stu_base_set.jpg','003_stu_base_set_seat_g.jpg',add_x=100,name='003_stu_base_set_seat_g.jpg')
        # 在上一个基础上增加1
        self.s.routine('003_stu_base_set.jpg', '003_stu_base_set_seat_g.jpg', add_y=110,name='003_stu_base_set_seat_g.jpg')
        # 提交
        self.s.routine('003_stu_base_set.jpg','003_stu_base_set_submit_g.jpg')
        self.s.routine('003_stu_base_set_save.jpg', '003_stu_base_set_save_replace_g.jpg')
        self.s.routine('003_stu_base_set.jpg', '003_stu_base_set_logout_g.jpg')
        time.sleep(10)




