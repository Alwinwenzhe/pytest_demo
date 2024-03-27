import pyautogui, time
from common.yaml_util import YamlUtil
from common.gui_common.cv_gui import CvGui


class GuiAnd(object):

    def __init__(self):
        self.cv = CvGui()
        pyautogui.PAUSE = 0.5  # 调用在执行动作后暂停的秒数
        pyautogui.FAILSAFE = True  # 启用自动防故障功能
        self.pic_path = r'./pic/jnt/'
        self.ya = YamlUtil()

    def get_screen(self, pic_name):
        '''获取某个时间段，电脑全屏截图'''
        self.cv.get_screenshot(self.pic_path + pic_name)

    def routine(self, source_name, goal_name, name='test', click='s', add_x=0, add_y=0):
        '''再次封装routine'''
        source_pic = self.pic_path + source_name
        goal_pic = self.pic_path + goal_name
        self.cv.routine(source_pic, goal_pic, name, click, add_x, add_y)

    def gui_click(self, source_pic, goal_pic, name='test', click='s'):
        '''点击截图位置中心区域'''
        self.routine(source_pic, goal_pic, name, click)

    def input_con(self, con):
        '''输入内容'''
        pyautogui.typewrite(con)

    def clear_and_input_con(self, con):
        '''清理并输入新内容'''
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press(['backspace'])
        pyautogui.typewrite(con)

    def log_out(self):
        '''
        点击：退出系统，前置条件：已经点击我的
        :return:
        '''
        self.routine('oa_home.png', 'oa_home_exit_sys.png', name='退出系统')  # 點擊退出系統
        self.routine('oa_home_exit.png', 'oa_home_exit_confirm.png', name='確認退出')


if __name__ == '__main__':
    ga = GuiAnd()
    ga.log_out()
