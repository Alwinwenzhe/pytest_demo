# -*- coding:utf-8 -*-
# Status:
# Time:

import pyautogui, time
from common.yaml_util import YamlUtil
from common.gui_common.cv_gui import CvGui

class S01(object):

    def __init__(self,root_path):
        self.cv = CvGui()
        pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数
        pyautogui.FAILSAFE = True  # 启用自动防故障功能
        self.pic_path = root_path + '/stu/'
        self.ya = YamlUtil()

    def get_screen(self,pic_name):
        '''获取某个时间段，电脑全屏截图'''
        self.cv.get_screenshot(self.pic_path + pic_name)

    def routine(self,source_name,goal_name,name='test',click='s',add_x=0,add_y=0):
        '''再次封装routine'''
        source_pic = self.pic_path + source_name
        goal_pic = self.pic_path + goal_name
        self.cv.routine(source_pic,goal_pic,name,click,add_x,add_y)

    def gui_click(self,source_pic,goal_pic,name='test',click='s'):
        '''点击截图位置中心区域'''
        self.routine(source_pic,goal_pic,name,click)

    def input_con(self,con):
        '''输入内容'''
        pyautogui.typewrite(con)

    def clear_and_input_con(self,con):
        '''清理并输入新内容'''
        pyautogui.hotkey('ctrl','a')
        pyautogui.press(['backspace'])
        pyautogui.typewrite(con)

    def get_exam_place(self):
        '''获取考点名'''
        return self.ya.read_extract_yaml('exam_place')

    def get_server_ip(self):
        '''获取配置文件中服务器ip'''
        self.ya.get_server_ip()

    def pre_exam(self):
        # 启动并设置校级服务器
        self.routine('001_pc_home.jpg', '001_pc_home_stu_client.png', click='d', name='001_pc_home_stu_client.png')
        time.sleep(3)
        self.routine('002_stu_home.jpg', '002_stu_home_set.jpg', name='002_stu_home_set.jpg')
        self.routine('002_stu_home_oper.jpg', '002_stu_home_oper_pwd.jpg', name='002_stu_home_oper_pwd.jpg')
        self.input_con('123456')
        self.routine('002_stu_home_oper.jpg', '002_stu_home_oper_enter.jpg', name='002_stu_home_oper_enter.jpg')
        time.sleep(2)
        # 修改校级服务器地址
        self.routine('003_stu_base_set.jpg', '003_stu_base_set_sch_server.jpg',
                       name='003_stu_base_set_sch_server.jpg')
        self.clear_and_input_con(self.get_server_ip())
        # 修改考点
        self.routine('003_stu_base_set.jpg', '003_tch_base_set_exam_place.jpg', add_x=200,
                       name='003_tch_base_set_exam_place.jpg')
        self.routine('003_tch_base_set_exam_place.jpg', '003_stu_base_set_exam_place_search.jpg',
                       name='003_stu_base_set_exam_place_search.jpg')
        self.input_con(self.get_exam_place())
        self.routine('003_tch_base_set_exam_place.jpg', '003_stu_base_set_exam_place_sch_g.jpg', add_y=100,
                       name='003_stu_base_set_exam_place_sch_g.jpg')
        # 默认物理考场
        # 座位号
        self.routine('003_stu_base_set.jpg', '003_stu_base_set_seat_g.jpg', add_x=100,
                       name='003_stu_base_set_seat_g.jpg')
        # 在上一个基础上增加1
        self.routine('003_stu_base_set.jpg', '003_stu_base_set_seat_g.jpg', add_y=110,
                       name='003_stu_base_set_seat_g.jpg')
        # 提交
        self.routine('003_stu_base_set.jpg', '003_stu_base_set_submit_g.jpg')
        self.routine('003_stu_base_set_save.jpg', '003_stu_base_set_save_replace_g.jpg')
        self.routine('003_stu_base_set.jpg', '003_stu_base_set_logout_g.jpg')
        time.sleep(6)

    def start_exam(self):
        '''开始考试'''
        pass

    def exam_main(self):
        '''考试入口'''
        self.pre_exam()
        self.start_exam()


if __name__ == '__main__':
    s = S01(r'../../../pic/xj')
    s.get_screen('002_tch_home.jpg')
    # s.gui_click('001_pc_home.jpg','001_pc_home_stu_client.png',click='d')