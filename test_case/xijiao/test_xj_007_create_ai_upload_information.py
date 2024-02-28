# -*- coding:utf-8 -*-
# Status:
# Time:

import pytest
from po.xj_kaoping.x04_exam_manage.xj06_create_exam_05_information_upload import Xj06CreateExam05InformationUpload
from selenium.webdriver.common.by import By

class TestXj007CreateAiUploadInformation(object):

    @pytest.mark.xj_smoke
    def test_001_upload_inform(self,open_browser):
        exam = Xj06CreateExam05InformationUpload(open_browser)
        exam.upload()
        assert exam.web.find_ele(By.CLASS_NAME,'siteBox')
