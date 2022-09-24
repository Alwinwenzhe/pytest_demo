# -*- coding:utf-8 -*-
# Status:
# Time:
import pytest, time
from selenium.webdriver.common.by import By

# @pytest.mark.usefixtures('open_url')    # 使用函数名open_url得fixture
@pytest.mark.usefixtures('refresh_page')    # fixture先引入得先执行，后引入后执行
@pytest.mark.demo
class TestLogin:

    pytestmark = pytest.mark.login  # 整个TestLogin类里面，所有测试用例都有login标签

    # 正常用例
    @pytest.mark.smoke
    def test_login_002_success(self,open_url):
        # 步骤--登录操作--登录页面--账号、密码
        d = open_url
        d.find_element(By.ID,'s-top-loginbtn').click()
        d.find_element(By.ID,'TANGRAM__PSP_11__userName').send_keys('18180734223')
        d.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys('225410weyd')
        d.find_element(By.ID,'TANGRAM__PSP_11__submit').click()
        time.sleep(9)



