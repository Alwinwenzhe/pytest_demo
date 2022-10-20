# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil


class Xj1102ExamSchoolDetail(object):

    # 学校名称
    school_name = (By.XPATH,'//td[@class="el-table_1_column_1.el-table__cell"]/div')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def get_school_name(self):
        '''获取学校名称'''
        name = self.web.find_ele(*self.school_name).text
        self.ya.write_inter_yaml('school_name',name)

