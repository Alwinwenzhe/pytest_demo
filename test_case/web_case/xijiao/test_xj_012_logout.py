# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x01_home.xj02_log_exit import XJ02LogExit
from selenium.webdriver.common.by import By

class TestXj012Logout(object):

    @pytest.mark.xj_smoke
    def test_log_out(self,open_browser):
        xj = XJ02LogExit(open_browser)
        xj.exit_login()
        assert xj.web.find_ele(By.NAME,'userName')
