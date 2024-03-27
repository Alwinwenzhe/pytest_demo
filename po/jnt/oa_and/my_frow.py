# -*- coding: utf-8 -*-
import time
from selenium.webdriver import Keys
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil
from common.operate_sql_al import OperateSqlAl
from selenium.webdriver.common.by import By
from common.operate_json import OperateJson
from po.jnt.oa_and.and_login import AndLogin


class MyFlow(object):
    '''oa审批'''

    oper_j = OperateJson()
    yam = YamlUtil()
    oper_s = OperateSqlAl('and_oa')

    url = '/#/workFlowManage/task/taskManagement'
    url = yam.read_extract_yaml('and_oa_url') + url
    chuchai_oa_name = '出差'  # 发起请假流程
    launch_oas = (By.CLASS_NAME, "ant-btn.ant-btn-primary", 1)  # 发起流程按钮
    search_oa_name = (By.CLASS_NAME, 'ant-input')  # 搜索框
    choose = (By.CLASS_NAME, 'el-icon.v-icon')  # 选择按钮前的+
    apply_message = (By.CLASS_NAME, 'el-icon-document')
    instance_name = (By.NAME, 'instanceName')  # 流程名字
    custome_name = 'Sele_' + chuchai_oa_name + "_" + str(oper_j.read_json()['cur_time_stf'])
    chuchai_start = (By.CLASS_NAME, 'cxd-DatePicker-input')
    chuchai_start_today = (By.CLASS_NAME, 'cxd-DatePicker-shortcut')
    scope = (By.CLASS_NAME, 'cxd-ResultBox-placeholder')  # 地域范围
    scope_list = (By.CLASS_NAME, 'cxd-ChainedSelection-itemLabel')  # 选择范围
    is_chengdu = (By.CLASS_NAME, 'cxd-Select-placeholder')  # 是否是成都
    choose_chengdu = (By.CLASS_NAME, 'cxd-Select-option-content')  # 选择是否
    transportation_mode = (By.CLASS_NAME, 'cxd-ResultBox-placeholder')  # 交通方式及工作承接人
    choose_transportation = (By.CLASS_NAME, 'cxd-ChainedSelection-itemLabel')  # 选择交通方式
    job_successor = (By.CLASS_NAME, 'cxd-ResultBox-placeholder')  # 工作承接人
    choose_successor = (By.CLASS_NAME, 'cxd-ChainedSelection-itemLabel')  # 选择员工
    reason_for_business_trip = (By.CLASS_NAME, 'cxd-TextareaControl-input')  # 出差原因及工作内容
    reason = '这个是自动化测试输入的出差原因，这个是自动化测试输入的出差原因，这个是自动化测试输入的出差原因！'
    job_content = '这个是自动化测试输入的工作内容，这个是自动化测试输入的工作内容，这个是自动化测试输入的工作内容！'
    submit = (By.CLASS_NAME, 'cxd-Button.cxd-Button--primary.cxd-Button--size-default')
    search_flow = (By.XPATH, '//input[@codefield="instanceName"]')  # 流程名字搜索框
    query_button = (By.CLASS_NAME, 'ant-btn.ant-btn-primary.mr-2')  # 查询按钮
    query_result = (By.XPATH, "//td[@title=" + "'" + custome_name + "'" + "]")  # 搜索结果

    list_detail = (By.CLASS_NAME, 'ant-btn.ant-btn-link.ant-btn-sm')  # 列表中的詳情按鈕
    next_approval = (By.XPATH, "//label[contains(., '数字智能研发部')]")  # 下一级审批人
    query_approval = 'SELECT su.username from system_users su WHERE su.nickname = "{}"'

    def __init__(self, driver):
        self.web = WebKey(driver)
        self.and_login = AndLogin(driver)

    def create_Business_trips(self):
        '''发起出差流程'''
        self.web.open(self.url)
        self.web.clicks(*self.launch_oas)
        self.web.send(*self.search_oa_name, self.chuchai_oa_name)
        self.web.simulation_key(Keys.RETURN)
        time.sleep(1)
        self.web.click(*self.choose)
        self.web.send(*self.instance_name, self.custome_name)
        self.web.click(*self.chuchai_start)
        self.web.click(*self.chuchai_start_today)
        self.web.dropdown_selects(*self.scope, *self.scope_list, 1)
        self.web.dropdown_selects(*self.is_chengdu, *self.choose_chengdu, 1)
        self.web.dropdown_selects(*self.transportation_mode, 0, *self.choose_transportation, 2)
        time.sleep(1)
        self.web.send(*self.reason_for_business_trip, self.reason, 0)
        self.web.dropdown_selects(*self.job_successor, *self.choose_successor, 0)
        self.web.send(*self.reason_for_business_trip, self.job_content, 1)
        self.web.click(*self.submit)

    def search_oa(self):
        '''
        通过发起的oa_name,搜索是否创建成功
        :param oa_name:
        :return:
        '''
        self.web.open(self.url)
        self.web.send(*self.search_flow, self.custome_name)
        self.web.click(*self.query_button)
        result = self.web.ele_exist(*self.query_result)
        return result

    def get_next_Approved_by(self):
        '''
        獲取當前流程的下一個審批人信息，傳遞給sql進行搜索賬號
        :return:
        '''
        self.web.open(self.url)
        self.web.clicks(*self.list_detail, 1)
        time.sleep(2)
        approval_pre = (self.web.find_eles(*self.next_approval)[0].text).split('\n')[0]  # 获取下级审批人
        approval = approval_pre.split("：")[1]
        self.query_approval = self.query_approval.format(approval)
        return self.oper_s.sql_main(self.query_approval)

    def log_in_flow(self, user, pwd):
        '''
        登錄操作
        :param user:
        :param pwd:
        :return:
        '''
        self.and_login.log_in(user, pwd)

    def log_out_flow(self):
        '''
        退出登錄
        :return:
        '''
        self.and_login.log_out()


if __name__ == '__main__':
    lo = MyFlow()
