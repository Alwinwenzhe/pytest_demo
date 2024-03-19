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
@allure.feature('建能通APP_正式环境')
@allure.severity('blocker')
class TestJntAppTest(object):
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

    @allure.story('APP登录模块')
    @pytest.mark.jnt_app
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'Login'))
    def test_01_app_login(self, case):
        self.new.test_case_method(case)

    @allure.story('安能达OA')
    @pytest.mark.jnt_app
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'AND'))
    def test_02_and_oa(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('OA模块')
    @pytest.mark.jnt_app
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'OA'))
    def test_03_app_oa(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('微博模块')
    @pytest.mark.jnt_app
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'weibo'))
    def test_04_app_weibo(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('维修模块')
    @pytest.mark.jnt_app
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'equip_repair'))
    def test_05_app_equip_repair(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('安能达OA')
    @pytest.mark.jnt_app
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'AND_close_oa'))
    def test_06_and_close_oa(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)

    @allure.story('首页模块')
    @pytest.mark.jnt_app
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('case', excel.get_excel_data("jnt_app_dev", 'app_home'))
    def test_07_app_home(self, case):
        self.d_time.write_time_to_json()
        self.new.test_case_method(case)


if __name__ == "__main__":
    a = str(list(range(10)))
    print(a)
