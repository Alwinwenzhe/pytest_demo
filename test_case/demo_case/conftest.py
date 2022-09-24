# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest, time
from selenium import webdriver

# @pytest.fixture(scope='session',autouse=True)
@pytest.fixture(scope="class")
def open_url():
    # 前置
    print("前置步骤开始运行>>>>>>>>>>>>>>>>>>>>>>")
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com') #url为链接地址
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver  #yield之前代码是前置，之后的代码就是后置。
    # 后置
    print('后置步骤开始运行>>>>>>>>>>>>>>>>>>>>>>')
    driver.quit()

# 刷新页面 - 定义的第二个fixture
@pytest.fixture
def refresh_page(open_url):
    print("执行完open_url前后置后，再执行下方代码")
    yield
    print("执行完refresh,再执行下方代码")
    open_url.refresh()          # yield 返回了driver，所以这里才能刷新
    time.sleep(10)
