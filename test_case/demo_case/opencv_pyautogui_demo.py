# -*- coding:utf-8 -*-
# Status: PASS
# Time:
import cv2, time
import pyautogui


class ImgAutoExec(object):
    '''
    通过opencv识别图片返回坐标
    pyautogui操作坐标
    '''

    def get_xy(self,goal_img_path):
        '''
        用来判定游戏画面的点击坐标
        :param img_model_path: 用来检测模板图片的路径
        :return: 以元组形式返回检测到的区域的中心坐标
        '''
        time.sleep(2)
        # 保存到当前目录下
        pyautogui.screenshot().save(r".\pic\pc_home.jpg")
        # 载入截图
        source_home = cv2.imread(r".\pic\pc_home.jpg")
        # 目标截图
        xj_teacher_pic = cv2.imread(goal_img_path)
        # 读取目标截图的高\宽
        heigh,width,channel = xj_teacher_pic.shape
        # 进行模板的匹配,最后的参数就是匹配方法
        result = cv2.matchTemplate(source_home,xj_teacher_pic,cv2.TM_SQDIFF_NORMED)
        # 解析匹配区域左上角坐标,返回四个坐标
        upper_left = cv2.minMaxLoc(result)[2]
        # 计算中心区域坐标:左上角坐标，加上1/2目标图片宽高
        return (upper_left[0] + int(width/2), upper_left[1] + int(heigh/2))


    def auto_sigle_click(self,loca):
        '''
        接受元组参数，自动点击
        :param loca: 坐标元组
        :return:
        '''
        pyautogui.click(loca[0],loca[1],button='left')
        time.sleep(1)

    def auto_double_click(self,loca):
        '''
        接受元组参数，自动点击两次
        :param loca: 坐标元组
        :return:
        '''
        pyautogui.doubleClick(*loca,button='left')
        time.sleep(1)

    def routine(self,goal_img_path,name):
        '''
        自动点击坐标入口
        :param goal_img_path: 目标图片路径
        :param name:
        :return:
        '''
        avg = self.get_xy(goal_img_path)
        print(f'正在点击{name}')        # f表示格式化字符串,在字符串里面使用用花括号括起来的变量和表达式
        self.auto_double_click(avg)


if __name__ == '__main__':
    img = ImgAutoExec()
    # img.routine(r".\pic\xj_teacher.png","教师端")
    img.routine(r"..\..\pic\xj_teacher.png","教师端")      # 相对路劲，寻找根目录下的pic文件夹