# -*- coding:utf-8 -*-
# Status:
# Time:
import pyautogui, time
from common.yaml_util import YamlUtil

class TC01(object):

    def __init__(self):
        pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数
        pyautogui.FAILSAFE = True  # 启用自动防故障功能
        self.ya = YamlUtil()

    def get_x_y(self):
        '''获取屏幕宽高'''
        x,y = pyautogui.size()
        return x,y

    def percent_x_y(self,goal_x,goal_y):
        '''通过当前屏幕及目标位置，算出目标相对位置'''
        pass

    def start_teacher(self):
        '''
        根据坐标启动教师端
        :param x: 3000
        :param y: 950
        :return:
        '''
        pyautogui.doubleClick(3000,950)
        time.sleep(5)

    def update_school_server(self):
        '''
        修改设置为167
        :return:
        '''
        time.sleep(3)
        self.enter_setting()
        # 修改校级服务器
        pyautogui.click(2129,585,duration=0.5)
        self.del_cont()
        pyautogui.typewrite(self.get_server_ip())
        time.sleep(3)

    def teacher_login(self):
        '''监考老师登录'''
        pyautogui.click(2093,924,duration=0.5)
        pyautogui.typewrite(self.ya.read_extract_yaml('invigi_teacher_id'))
        # 密码
        pyautogui.click(2106,1076,duration=0.5)
        pyautogui.typewrite('123456')
        pyautogui.click(2303,1277,duration=0.5)

    def enter_setting(self):
        # 进入基本设置
        pyautogui.click(3100, 70)
        time.sleep(2)
        pyautogui.click(1485, 974, duration=0.5)
        pyautogui.typewrite('123456')
        pyautogui.click(1885, 1193, duration=0.5)
        time.sleep(1)

    def get_server_ip(self):
        '''获取校级服务器ip'''
        server_ip = self.ya.read_extract_yaml('ip')
        ser_ip = (server_ip.split("//")[1]).split(":")[0]
        ser_ip = ser_ip + ":" + "8080"
        return ser_ip

    def log_out(self):
        '''退出登录'''
        pyautogui.click(2975, 70, duration=0.5)
        time.sleep(1)
        pyautogui.click(1795,1159, duration=0.5)

    def del_cont(self):
        '''删除目标内容'''
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press(['backspace'])

    def invig_audit(self):
        '''一键验证座位'''
        pyautogui.click(2406,834,duration=0.5)
        time.sleep(3)
        # 一键验证
        pyautogui.click(2504,204,duration=0.5)
        time.sleep(1)
        pyautogui.click(1786,1153,duration=0.5)
        self.close_exe()

    def close_exe(self):
        '''
        关闭程序
        :return:
        '''
        time.sleep(1)
        pyautogui.hotkey('fn','alt','F4')

    def print_cur_location(self):
        '''打印当前位置'''
        for i in range(1,4):
            print("找好位置，计时3s：{0}s".format(i))
            time.sleep(1)
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

    def teache_audit(self):
        '''
        监考老师一键验证
        :return:
        '''
        pyautogui.hotkey('win', 'd')
        time.sleep(3)
        self.start_teacher()
        self.update_school_server()
        self.teacher_login()
        self.invig_audit()


if __name__ == '__main__':
    tc = TC01()
    tc.print_cur_location()
    # tc.teache_audit()