# -*- coding:utf-8 -*-
# Status: PASS
# Time:
import cv2, time
import pyautogui


class CvGui(object):
    '''
    通过opencv识别图片返回坐标
    pyautogui操作坐标
    '''
    def get_screenshot(self,name):
        '''获取当前屏幕截图,保存到指定路径'''
        pyautogui.screenshot().save(name)

    def get_xy(self,sour_img,goal_img,add_x=0,add_y=0):
        '''
        用来判定目标元素的坐标
        :param img_model_path: 用来检测模板图片的路径
        :param sour_img_path: 源图片路径
        :return: 以元组形式返回检测到的区域的中心坐标
        :param add_x: 在图片X坐标基础上增加坐标值，弥补非唯一性带来得差距
        :param add_y: 在图片Y坐标基础上增加坐标值，弥补非唯一性带来得差距
        :return:
        '''
        # 载入源截图
        source_home = cv2.imread(sour_img)
        # 目标截图
        goal_pic = cv2.imread(goal_img)
        # 读取目标截图的高\宽,channel？
        heigh,width,channel = goal_pic.shape
        # 进行模板的匹配,最后的参数就是匹配方法
        result = cv2.matchTemplate(source_home,goal_pic,cv2.TM_SQDIFF_NORMED)
        # 解析匹配区域左上角坐标,返回四个坐标
        upper_left = cv2.minMaxLoc(result)[2]
        # 计算中心区域坐标:左上角坐标，加上1/2目标图片宽高
        return (upper_left[0] + int(width/2) + add_x, upper_left[1] + int(heigh/2) + add_y)

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

    def routine(self,source_img,goal_img_path,name='学生端',click_type='s',add_x=0,add_y=0):
        '''
        自动点击坐标入口
        :param goal_img_path: 目标图片路径
        :param name:
        :return:
        '''
        avg = self.get_xy(source_img,goal_img_path,add_x,add_y)
        print(f'正在点击{name}')        # f表示格式化字符串,在字符串里面使用用花括号括起来的变量和表达式
        if click_type == "d":
            self.auto_double_click(avg)
        else:
            self.auto_sigle_click(avg)



if __name__ == '__main__':
    img = CvGui()
    # img.routine(r".\pic\xj_teacher.png","教师端")
    # img.routine(r"..\..\pic\xj_teacher.png","教师端")      # 相对路劲，寻找根目录下的pic文件夹
    img.get_screenshot(r'..\..\pic\xj\tch\pc_home.jpg')
    # print(img.get_xy(r"..\..\pic\xj\stu\001_pc_home.jpg",r'..\..\pic\xj\stu\001_pc_home_stu_client.png'))