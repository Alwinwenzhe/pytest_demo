import pyautogui, time
from common.yaml_util import YamlUtil

pyautogui.PAUSE = 1 # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常



class Demo(object):

    ya = YamlUtil()

    def start_stu_client(self):
        '''启动学生端'''
        pyautogui.doubleClick(3122,920,duration=0.5)
        time.sleep(5)

    def update_setting(self):
        '''登录及修改设置主入口'''
        time.sleep(2)
        self.start_stu_client()
        self.enter_setting()
        self.update_school_server()
        self.update_exam_place()


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
        time.sleep(1)

    def update_exam_place(self):
        '''更新考点'''
        pyautogui.click(1772,945,duration=0.5)
        time.sleep(1)
        # 考点
        pyautogui.click(1822,1086,duration=0.5)
        pyautogui.typewrite(self.ya.read_extract_yaml('school_name'))
        time.sleep(1)
        pyautogui.click(1888,1327,duration=0.5)
        # 考场--这里写死了，照理应该参数控制
        pyautogui.click(1805,1244,duration=1)
        self.close_exe()
        # 提交
        pyautogui.click(1674,1634,duration=0.5)
        time.sleep(1)
        pyautogui.click(1791,1206,duration=0.5)
        self.reback()

    def choose_site(self):
        '''选择座位'''
        pyautogui.click(1743,1303,duration=0.5)
        time.sleep(1)
        # 座位1
        pyautogui.click(1732,1429,duration=0.5)

    def reback(self):
        '''返回'''
        pyautogui.click(3112,69,duration=0.5)

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

    def del_cont(self):
        '''删除目标内容'''
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press(['backspace'])

    def close_exe(self):
        '''
        关闭程序
        :return:
        '''
        time.sleep(1)
        pyautogui.hotkey('fn', 'alt', 'F4')

    def print_cur_location(self):
        '''打印当前位置'''
        for i in range(1,4):
            print("找好位置，计时3s：{0}s".format(i))
            time.sleep(1)
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

if __name__ == '__main__':
    de = Demo()
    de.print_cur_location()
    # de.update_setting()
    # pyautogui.doubleClick(3126,918,duration=0.5)