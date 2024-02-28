    # -*- coding:utf-8 -*-
    # Status:  调试中，
    # Time:

from appium import webdriver
from time import sleep
from test_case.app_case.conftest import android_driver


class TestAddArticle(object):

    def __init__(self):
        self.driver = android_driver(0)

    def add_article(self):
        '''
        新增文章
        :return:
        '''
        sleep(6)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("微评")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').send_keys(
            "今天又花了4099元\n要努力赚钱呀！")
        # 这里看是否要切换到frame
        sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.sina.weibo:id/iv_edit_pic")').click()
        sleep(1)
        # 点击相册
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.sina.weibo:id/photo_album_title_icon")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("test")').click()
        # 选择照片,注意这里的多个结果，该使用什么方法和定位
        self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("com.sina.weibo:id/photo_album_grideview_item_select")')[0].click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加标题")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("填写标题")').send_keys("花钱真爽")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("选择")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').send_keys("自考")
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击添加物品话题")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        sleep(10)


    def test_operate(self):
        '''
        滑动浏览视频
        :return:
        '''
        self.add_article()
        sleep(3)  # 这里不等待时间很有可能两个滑动至生效一个

if __name__ == '__main__':
    driver = TestAddArticle()
    while 1:
        driver.test_operate()