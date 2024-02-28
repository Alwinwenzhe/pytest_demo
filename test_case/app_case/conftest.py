import threading, time, pytest
from appium import webdriver
from common.app_common.write_user_command import WriteUserCommand
from common.app_common.app_server import AppServer

wuc = AppServer()

def and_server():
    '''启动命令行服务'''
    wuc.start_appium_server_thread()

def android_driver(i):
    wuc = WriteUserCommand()
    device_name = wuc.get_yaml('user_info_{}'.format(str(i)), 'devicesname')
    port = wuc.get_yaml('user_info_{}'.format(str(i)), 'b')
    capabilities = {
        "platformName": "Android",
        "deviceName": device_name,
        "appActivity": "com.sina.weibo.MainTabActivity",
        # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
        "appPackage": "com.sina.weibo",
        "noReset": True,
        'automationName': 'Uiautomator2',  # 定位toast元素就需要写
        'unicodeKeyboard': True,
        'newCommandTimeout': '60000'  # 超时设置，appium保持余设备连接
    }
    # 运行前命令行启动：appium -p 4725 -bp 5000
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port), capabilities)
    driver.implicitly_wait(15)  # 全局设置，每个元素最长等待时间10s
    return driver

def thread_app_driver():
    '''
    多线程启动driver,直接这样启动不知道煤气启动一个driver怎么返回
    :return:
    '''
    for i in range(len(wuc.dev_list)):
        appium_start = threading.Thread(target=android_driver,args=(i,))      # 注意这里启动方式
        appium_start.start()
        time.sleep(13)

@pytest.fixture(scope='session',autouse=True)
def start_server_and_driver():
    '''多线程启动server与driver'''
    and_server()
    thread_app_driver()

if __name__ == '__main__':
    start_server_and_driver()



