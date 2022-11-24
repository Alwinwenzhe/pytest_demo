# -*- coding:utf-8 -*-
# Status:
# Time:
import pyautogui, time
from common.gui_common.cv_gui import CvGui
from common.yaml_util import YamlUtil

class TC01(object):

    def __init__(self,root_path):
        self.cv = CvGui()
        pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数
        pyautogui.FAILSAFE = True  # 启用自动防故障功能
        self.pic_path = root_path + '/tch/'
        self.ya = YamlUtil()

    def start_teacher(self):
        '''
        启动教师端
        :return:
        '''
        self.routine('001_pc_home.jpg','001_pc_home_tch_g.jpg',name='001_pc_home_tch_g.jpg',click='d')
        time.sleep(3)

    def click_tch_home_set(self):
        '''点击设置并输入鉴权密码'''
        self.routine('002_tch_home.jpg','002_tch_home_set_g.jpg',name='002_tch_home_set_g.jpg')
        time.sleep(1)
        self.routine('002_tch_home_oper.jpg','002_tch_home_oper_pwd_g.jpg',name='002_tch_home_oper_pwd_g.jpg')
        time.sleep(1)
        pyautogui.typewrite('123456')
        self.routine('002_tch_home_oper.jpg','002_tch_home_oper_enter_g.jpg',name='002_tch_home_oper_enter_g.jpg')
        time.sleep(3)

    def update_base_set(self):
        '''更新基本设置'''
        self.routine('003_set_base.jpg','003_set_base_sch_ser_g.jpg',name='003_set_base_sch_ser_g.jpg',add_x=100)
        time.sleep(1)
        self.clear_and_input_con(self.ya.get_server_ip())
        time.sleep(2)
        # 修改考点
        self.routine('003_tch_base_set_exam_place.jpg', '003_tch_base_set_exam_place_g.jpg', add_x=100,name='003_tch_base_set_exam_place_g.jpg')
        self.routine('003_stu_base_set_exam_place_search.jpg', '003_stu_base_set_exam_place_search_g.jpg',name='003_stu_base_set_exam_place_search_g.jpg')
        time.sleep(1)
        pyautogui.typewrite(self.ya.read_extract_yaml('exam_place'))
        self.routine('003_stu_base_set_exam_place_search.jpg', '003_stu_base_set_exam_place_search_rlt_g.jpg', add_y=100,name='003_stu_base_set_exam_place_search_rlt_g.jpg')
        pyautogui.click(3000, 1000)
        time.sleep(1)
        # 考场修改
        self.routine('003_set_base.jpg', '003_tch_base_set_exam_sub_g.jpg', add_x=200, name='003_set_base_sub_g.jpg')
        self.routine('003_tch_base_set_exam_sub.jpg', '003_tch_base_set_exam_sub_list_g.jpg', add_y=-80,
                   name='003_tch_base_set_exam_sub_list_g.jpg')
        # 保存退出
        time.sleep(1)
        self.routine('003_set_base.jpg', '003_set_base_submit_g.jpg', name='003_set_base_submit_g.jpg', )
        self.routine('003_stu_base_set_update.jpg', '003_stu_base_set_update_close_g.jpg',
                   name='003_stu_base_set_update_close_g.jpg')
        self.routine('003_set_base.jpg', '003_set_base_logout_g.jpg', name='003_set_base_logout_g.jpg')

    def clear_and_input_con(self,con):
        '''清理并输入新内容'''
        pyautogui.hotkey('ctrl','a')
        pyautogui.press(['backspace'])
        pyautogui.typewrite(con)

    def print_cur_location(self):
        '''打印当前位置'''
        for i in range(1,4):
            print("找好位置，计时3s：{0}s".format(i))
            time.sleep(1)
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

    def routine(self,source_name,goal_name,name='test',click='s',add_x=0,add_y=0):
        '''再次封装routine'''
        source_pic = self.pic_path + source_name
        goal_pic = self.pic_path + goal_name
        self.cv.routine(source_pic,goal_pic,name,click,add_x,add_y)

    def teacher_login(self):
        '''老师登录'''
        time.sleep(1)
        self.routine('002_tch_home.jpg','002_tch_home_user_g.jpg')
        pyautogui.typewrite(self.ya.read_extract_yaml('invigi_teacher_id'))
        self.routine('002_tch_home.jpg','002_tch_home_pwd_g.jpg')
        pyautogui.typewrite('123456')
        self.routine('002_tch_home.jpg','002_tch_home_login_g.jpg')
        time.sleep(2)

    def batch_verify(self):
        '''批量验证'''
        pass

    def get_screen(self,pic_name):
        '''获取某个时间段，电脑全屏截图'''
        self.cv.get_screenshot(self.pic_path + pic_name)

    def seat_invit(self):
        '''座位一键验证'''
        time.sleep(1)
        self.routine('004_examing.jpg','004_examing_seat_invit_g.jpg')
        time.sleep(1)
        self.routine('005_inviting.jpg','005_inviting_batch_verify_g.jpg')
        self.routine('005_inviting_confirm.jpg','005_inviting_confirm_ok_g.jpg')
        pyautogui.hotkey('fn','alt','f4')

    def teache_audit(self):
        '''
        监考老师一键验证
        :return:
        '''
        pyautogui.hotkey('win', 'd')
        time.sleep(1)
        self.start_teacher()
        self.click_tch_home_set()
        self.update_base_set()
        self.teacher_login()
        self.seat_invit()


if __name__ == '__main__':
    tc = TC01(r'../../../pic/xj')
    time.sleep(1)
    # tc.teache_audit()
    tc.get_screen('005_inviting_confirm.jpg')
