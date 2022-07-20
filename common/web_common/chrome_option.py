# -- coding:utf-8 --
'''
    Chrome浏览器的配置：
        通过webdriver启动的浏览器默认是零缓存(不读取本地缓存数据)的浏览器，相当于隐身浏览器
        options没有任何技术含量，所有内容都是写死的
        一般就是一次编写，以后固定使用
'''
from selenium import webdriver
from time import sleep


class ChromeOptions:

    profile_directory = r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

    def options(self):
        # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器形态
        options = webdriver.ChromeOptions()
        # 将浏览器默认设置为最大窗体
        options.add_argument('start-maximized')
        # 去掉默认提示自动化信息：警告条有可能会导致页面内容遮挡
        # options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ['enable - automation'])
        # 老版本去掉警告条的参数，已经不生效了
        #options.add_argument('disable-infobars')
        # 读取本地缓存，实现一个有缓存的浏览器，这个指令执行前必须关闭所有本地的chrome浏览器
        #options.add_argument(self.profile_directory)
        # 去掉账号密码弹窗
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enabled'] =False
        options.add_experimental_option('prefs',prefs)
        sleep(1)
        return options