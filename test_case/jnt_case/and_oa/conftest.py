import pytest
from selenium.webdriver.common.by import By
from common.web_common.chrome_option import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session', autouse=True)
def open_browser(type_='Firefox'):
    '''基于type_值决定生成的driver对象是什么类型'''
    print('会话之前初始化diriver')
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=ChromeOptions().options())
    elif type == 'Firefox':
        # 使用 webdriver-manager 来自动下载和管理 GeckoDriver
        # 这样可以避免手动下载和配置 GeckoDriver
        service = Service(GeckoDriverManager().install())
        # 初始化 Firefox WebDriver
        driver = webdriver.Firefox(service=service)
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            print("Exception Information:", str(e))
            driver = webdriver.Chrome()
    return driver

# @pytest.fixture(scope='module',autouse=True)
# def init_driver():
#     '''会话之前初始化diriver'''
#     print('会话之前初始化diriver')
#     yield
#     print('会话之前结束db')
