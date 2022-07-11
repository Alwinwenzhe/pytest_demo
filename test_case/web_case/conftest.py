import pytest
from po.xj_kaoping.login import Login
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.web_common.chrome_option import ChromeOptions

@pytest.fixture(scope='session',autouse=True)
def open_browser(type_='Chrome'):
    '''基于type_值决定生成的driver对象是什么类型'''
    print('会话之前初始化diriver')
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=ChromeOptions().options())
    else:
        try:
            driver = getattr(webdriver,type_)()
        except Exception as e:
            print("Exception Information:",str(e))
            driver = webdriver.Chrome()
    return driver

# @pytest.fixture(scope='module',autouse=True)
# def init_driver():
#     '''会话之前初始化diriver'''
#     print('会话之前初始化diriver')
#     yield
#     print('会话之前结束db')
