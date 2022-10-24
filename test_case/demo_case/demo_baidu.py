# -*- coding:utf-8 -*-
# Status:
# Time:

import pyautogui,time

if __name__ == '__main__':

    time.sleep(3)
    print('即将在鼠标当前位置点击两次，间隔0.25s')
    pyautogui.click(x=100,y=100,button='left')               # 可用于打开某个应用

