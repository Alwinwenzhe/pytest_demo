# -*- coding:utf-8 -*-
# Status:
# Time:

import pyautogui, time
from common.yaml_util import YamlUtil
from common.gui_common.cv_gui import CvGui

class S01(object):

    def __init__(self,root_path):
        self.cv = CvGui()
        # self.pic_path = r'../../../pic/xj/stu/'
        self.pic_path = root_path
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

    def get_server_ip(self):
        '''获取校级服务器ip'''
        server_ip = self.ya.read_extract_yaml('ip')
        ser_ip = (server_ip.split("//")[1]).split(":")[0]
        ser_ip = ser_ip + ":" + "8080"
        return ser_ip

    def get_exam_place(self):
        '''获取考点名'''
        return self.ya.read_extract_yaml('exam_place')


if __name__ == '__main__':
    s = S01(r'../../../pic/xj/stu/')
    s.get_screen('003_stu_base_set_save.jpg')
    # s.gui_click('001_pc_home.jpg','001_pc_home_stu_client.png',click='d')