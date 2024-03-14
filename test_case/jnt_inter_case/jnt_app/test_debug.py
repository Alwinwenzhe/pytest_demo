# Comment：通过excel管理测试用例
# Status:pass
import allure, pytest, os, sys
from common import deal_json
from common import excel_handler
from common import deal_time


# @allure.feature('ysy_Login')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
# @allure.severity('blocker')  # allure.severity 用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
# # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
# @allure.story('Get_Verifycode')  # allure.story  用于定义被测功能的用户场景，即子功能点
@allure.feature('调试demo')
class TestDebug(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = excel_handler.ExcelHandler()
    new = deal_json.DealJson()
    d_time = deal_time.DealTime()

    @allure.step('APP_登录')
    @pytest.mark.debug
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("debug", "Login"))
    def test_001_debug(self, case):
        self.new.test_case_method(case)

    @allure.step('OA')
    @pytest.mark.debug
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("debug", "OA"))
    def test_002_oa(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('微博模块')
    @pytest.mark.debug
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("debug", 'weibo'))
    def test_app_weibo(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('安能达OA')
    @pytest.mark.debug
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("debug", 'AND'))
    def test_app_weibo(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('维修模块')
    @pytest.mark.debug
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("debug", 'equip_repair'))
    def test_app_weibo(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)


if __name__ == "__main__":
    a = str(list(range(10)))
    print(a)
