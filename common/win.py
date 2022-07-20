# -*- coding:utf-8 -*-
# Status:
# Time:
import time
from pywinauto import Desktop


def win_upload(location):
    '''
    windows弹窗上传文件
    :param location: 文件位置，如：J:\now_job\西交智慧\基础数据\成都七中\成都七中_东区总校_cwz_学生_half.xlsx
    :return:
    '''
    upload = Desktop()
    dialog = upload['打开']       # 根据名字找到弹出窗口
    dialog['Edit'].type_keys(location)      # 在输入框中输入值
    time.sleep(3)
    dialog['button'].click()

if __name__ == '__main__':
    win_upload(r'J:\now_job\西交智慧\基础数据\成都七中\成都七中_东区总校_cwz_学生_half.xlsx')