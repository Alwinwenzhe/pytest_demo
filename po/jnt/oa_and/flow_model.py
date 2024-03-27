# -*- coding: utf-8 -*-
import time
from selenium.webdriver import Keys
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil
from selenium.webdriver.common.by import By
from common.operate_json import OperateJson
from po.jnt.oa_and.and_login import AndLogin


class MyFlow(object):
    '''oa审批'''

    oper_j = OperateJson()
    yam = YamlUtil()

    url = '/#/workFlowManage/workFlow/processModel'

    def __init__(self, driver):
        self.web = WebKey(driver)
        self.and_login = AndLogin(driver)

    def search_flow_mode(self, model_name):
        '''
        通過流程模型名字搜索，並確定對應的分配人
        :param model_name:
        :return:
        '''
        url = self.yam.read_extract_yaml('and_oa_url') + self.url
        self.web.open(url)
