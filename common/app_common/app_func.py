# Debug_time:  2020-11-22
# Status:

# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

from appium import webdriver
from time import sleep
from datetime import datetime
import random


class DebugTikTok(object):

    def __init__(self,driver):
        self.driver = driver

    # 获取屏幕宽高
    def get_size(self):
        size = self.driver.get_windows_sizes()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动：
    def swip_left(self):
        """
        此方法适合在顶部banner位置进行滑动
        :return:
        """
        x = self.get_size[0] / 10 * 9
        y = self.get_size[1] / 10 * 2
        x1 = self.get_size[0] / 10 * 4
        self.driver.swipe(x, y, x1, y)

    def swip_right(self):
        x = self.get_size[0] / 10 * 1
        y = self.get_size[1] / 10 * 2
        x1 = self.get_size[0] / 10 * 9
        driver.swipe(x, y, x1, y)

    def swip_up(self):
        '''
        此方法是从底部往上滑动
        :return:
        '''
        x = self.get_size()[0] / 10 * 1
        y = self.get_size()[1] / 10 * 8
        y1 = self.get_size()[1] / 10 * 4
        self.driver.swipe(x, y, x, y1)

    def swip_down(self):
        '''
        向下滑动
        :return:
        '''
        x = self.get_size()[0] / 10 * 2
        y = self.get_size()[1] / 10 * 2
        y1 = self.get_size()[1] / 10 * 7
        self.driver.swipe(x, y, x, y1)

    def swip_on(self, direction):
        '''
        再次封装4个滑动方法:up,down,left,right
        :return:
        '''
        if direction == 'up':
            self.swip_up()
        elif direction == 'down':
            self.swip_down()
        elif direction == 'left':
            self.swip_left()
        elif direction == 'right':
            self.swip_right()
        else:
            print('noting swip!!!')

    def sleep_random(self):
        '''
        等待等待时间
        :return:
        '''
        sleep_time = random.randrange(1, 20)
        return sleep_time

    def get_time(self):
        '''
        获取当前时间戳
        :return:
        '''
        return datetime.now(self)

    def time_compare_1(self):
        '''
        时间对比
        :return:
        '''
        t1 = self.get_time()
        t3 = 0
        while t3 < 1280:
            self.operate()
            t2 = self.get_time()
            t3 = t2 - t1
        else:
            self.operator_coin()
            t3 = 10

    def operator_coin(self):
        '''
        获取金币操作
        :return:
        '''

    def operate(self):
        '''
        滑动浏览视频
        :return:
        '''
        self.swip_on("up")
        print('reset random seconds:-------')
        sleep(self.sleep_random())  # 这里不等待时间很有可能两个滑动至生效一个


if __name__ == '__main__':
    # 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
    # command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
    # doc_cmd = Doc_Cmd()
    # doc_cmd.excute_cmd(command)
    # # sleep(8)
    driver = DebugTikTok()
    driver.swip_on("up")
    print('reset random seconds:-------')

