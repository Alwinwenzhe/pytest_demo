import pytest
from po.xj_kaoping.login import Login
from selenium.webdriver.common.by import By

# login = Login()
#
# @pytest.fixture(scope='module',autouse=True)
# @pytest.mark.xijiao
# # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
# @pytest.mark.parametrize('name,pwd', [['admin', '123123'], ['admin', '123456']])
# def init_driver_xj_log_in(name, pwd):
#     """
#         用例描述：获取验证码
#     """
#     login.log_in(name, pwd)
#     assert login.web.assert_text(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span',
#                                       '系统管理')

@pytest.fixture(scope='module',autouse=True)
def init_driver():
    '''会话之前初始化diriver'''
    print('会话之前初始化diriver')
    yield
    print('会话之前结束db')
