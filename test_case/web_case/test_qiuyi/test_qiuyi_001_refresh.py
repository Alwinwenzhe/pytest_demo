# -*- coding:utf-8 -*-
import allure, pytest, os, sys
from common import deal_json
from common import excel_handler


# @allure.feature('ysy_Login')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
# @allure.severity('blocker')  # allure.severity 用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
# # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
# @allure.story('Get_Verifycode')  # allure.story  用于定义被测功能的用户场景，即子功能点
@allure.feature('求艺网')
@allure.severity('blocker')
@allure.story('刷新贴子')
class TestQiuyi001refresh(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = excel_handler.ExcelHandler()
    new = deal_json.DealJson()

    # excel.get_excel_data() 传参需要确认
    # @pytest.mark.smoke
    # # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    # @pytest.mark.parametrize('case', excel.get_excel_data())
    # def test_login_001_get_verifycode(self,case):
    #     """
    #         用例描述：获取验证码
    #     """
    #     self.new.write_data_to_json()       # 初始化相关数据
    #     self.new.test_case_method(case)