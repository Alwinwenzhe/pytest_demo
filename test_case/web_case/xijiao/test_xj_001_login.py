# Status：PASS
# TIME：2022_07_07
import pytest
from po.xj_kaoping.x01_home.login import Login
from selenium.webdriver.common.by import By



class TestXJ001Login:

    @pytest.mark.skip
    @pytest.mark.xijiao
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    # @pytest.mark.parametrize('name,pwd,result', [['admin','123123',False],['admin','123456',True]])
    def test_xj_login_001(self,open_browser, name='admin',pwd='123123',result=False):
        """
            用例描述：获取验证码
        """
        login = Login(open_browser)
        login.log_in(name,pwd,open_browser)
        assert result == login.web.assert_text(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span','系统管理')

    @pytest.mark.xj_smoke
    def test_xj_login_002(self,open_browser, name='admin',pwd='123456',result=True):
        """
            用例描述：获取验证码
        """
        login = Login(open_browser)
        login.log_in(name,pwd,open_browser)
        assert result == login.web.assert_text(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span','系统管理')

if __name__ == '__main__':
    print(TestXJ001Login().test_xj_login_001)