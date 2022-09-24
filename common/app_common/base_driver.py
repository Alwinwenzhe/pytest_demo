# -- coding:utf-8 --
from appium import webdriver
from common.app_common.write_user_command import WriteUserCommand

class BaseDriver(object):

    def android_driver(self,i):
        wuc = WriteUserCommand()
        device_name = wuc.get_yaml('user_info_{}'.format(str(i)),'devicesname')
        port = wuc.get_yaml('user_info_{}'.format(str(i)), 'b')
        capabilities = {
            "platformName": "Android",
            "deviceName": device_name,
            "appActivity": "com.jmbon.android.view.WelcomeActivity",
        # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.jmbon.android",
            "noReset": "True",
            'automationName': 'Uiautomator',  # 定位toast元素就需要写
            'unicodeKeyboard': True,
            'newCommandTimeout': '150000'  # 超时设置，appium保持余设备连接
        }
        # 运行前命令行启动：appium -p 4725 -bp 5000
        driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port), capabilities)
        driver.implicitly_wait(15)  # 全局设置，每个元素最长等待时间10s
        return driver

    def ios_driver(self):
        pass

if __name__ == '__main__':
    bd = BaseDriver()

