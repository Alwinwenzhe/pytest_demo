import pytest, allure
from common.deal_time import DealTime
from po.jnt.oa_and.my_frow import MyFlow


class TestAnd002OaApproval:
    shared_value = None
    d_time = DealTime()

    @allure.story('AND')
    @allure.suite('OA')
    @allure.step('发起出差流程')
    @pytest.mark.andoa
    def test_001_andoa_create_chuchai(self, open_browser, name='chenwenzhe', pwd='123456'):
        """
            用例描述：创建出差流程
        """
        self.d_time.write_time_to_json()
        oa = MyFlow(open_browser)
        oa.log_in_flow(name, pwd)
        oa.create_Business_trips()
        self.shared_value = oa.get_next_Approved_by()
        assert True == oa.search_oa()

    @pytest.mark.andoa
    def test_002_exit_oa(self, open_browser):
        '''只是推出'''
        oa = MyFlow(open_browser)
        oa.log_out_flow()

    @pytest.mark.andoa
    def test_003_Approval_chuchai(self, open_browser):
        oa = MyFlow(open_browser)
        oa.log_in_flow(self.shared_value, '123456')


if __name__ == '__main__':
    print(TestAnd002OaApproval().test_001_andoa_create_chuchai())
