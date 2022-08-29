# -*- coding:utf-8 -*-
# Status:
# Time:
import time ,win32gui, win32con
from pywinauto import Desktop


# def win_upload(location):
#     '''
#     windows弹窗上传文件
#     :param location: 文件位置，如：J:\now_job\西交智慧\基础数据\成都七中\成都七中_东区总校_cwz_学生_half.xlsx
#     :return:
#     '''
#     upload = Desktop()
#     time.sleep(1)
#     dialog = upload['打开']       # 根据名字找到弹出窗口
#     dialog['Edit'].type_keys(location)      # 在输入框中输入值
#     dialog['button'].click()
#     time.sleep(1)

def win_upload(location):
    '''
       :param file_path:上传文件的路径
       :return:
       '''
    dialog = win32gui.FindWindow("#32770", "打开")
    comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
    edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, location)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

if __name__ == '__main__':
    win_upload(r'J:\now_job\西交智慧\基础数据\学校\AT_高新-3\成都七中\成都七中_东区总校_cwz_巡考老师.xlsx')