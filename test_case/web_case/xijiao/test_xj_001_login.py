# Status：PASS
# TIME：2022_07_07
import pytest,time
from po.xj_kaoping.login import Login
from selenium.webdriver.common.by import By



class TestXJ001Login:



    @pytest.mark.xijiao
    # @pytest.mark.parametrize()第一个参数为逗号分隔的字符串列表，第二个参数是值列表parametrize()
    @pytest.mark.parametrize('name,pwd', [['admin','123123'],['admin','123456']])
    def test_xj_login_001_get_verifycode(self, name,pwd,open_browser):
        """
            用例描述：获取验证码
        """
        login = Login(open_browser)
        login.log_in(name,pwd,open_browser)
        assert login.web.assert_text(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span','系统管理')


if __name__ == '__main__':
    print(TestXJ001Login().test_xj_login_001_get_verifycode)