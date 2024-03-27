import pytest, allure
from selenium.webdriver.common.by import By

from po.jnt.oa_and.and_login import AndLogin


class TestAnd001Login:

    @allure.story('登录模块')
    @allure.suite('OA')
    @allure.step('登录')
    @pytest.mark.andoa
    @pytest.mark.skip
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    # @pytest.mark.parametrize('name,pwd,result', [['admin','123123',False],['admin','123456',True]])
    def test_andoa_login_001(self, open_browser, name='chenwenzhe', pwd='123456', result=True):
        """
            用例描述：获取验证码
        """
        login = AndLogin(open_browser)
        login.log_in(name, pwd)
        assert result == login.web.assert_text(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div',
                                               '安能达管理系统')


if __name__ == '__main__':
    print(TestAnd001Login().test_andoa_login_001())
