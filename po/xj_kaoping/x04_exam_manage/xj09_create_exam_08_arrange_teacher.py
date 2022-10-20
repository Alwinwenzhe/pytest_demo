# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium.webdriver.common.by import By
from common.web_common.web_key import WebKey
from common.yaml_util import YamlUtil

class Xj09CreateExam08ArrangeTeacher(object):

    url ='http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 安排监考老师
    invigilation_area = (By.CLASS_NAME,'siteBox')
    # 选择姓名
    name_tab = (By.XPATH,'//span[contains(text(),"按姓名")]')
    # 监考checkbox
    invit_teachers = (By.XPATH,'//span[@class="el-checkbox__inner"]')
    # 组长自动分配
    auto = (By.XPATH,'//div[@class="leader"]/div[1]')
    # 确定
    # enter_js = 'document.getElementsByClassName("el-button el-button--primary el-button--medium")[4]'
    enter_js = (By.XPATH,'//span[text()="确定"]')
    # 获取第8个监考老师身份证号
    invigilation_last_id = (By.XPATH,'//tr[@class="el-table__row"][3]/td[3]/div')

    # 安排阅卷老师
    marking_teacher = (By.ID,'tab-reviewTeacher')
    marking_area = (By.XPATH,'//div[@class="el-tabs__content"]/div[2]/div/div[2]/div')
    # 获取阅卷老师第6个身份证
    marking_last_id = (By.XPATH,'//tr[@class="el-table__row"][6]/td[3]/div')

    # 安排巡考老师
    inspector_teacher = (By.ID,'tab-inspectorTeacher')
    inspector_area = (By.XPATH,'//div[@class="el-tabs__content"]/div[3]/div/div[2]/div')

    # 保存并完成
    save = (By.XPATH,'//span[text()=" 保存并完成考试计划 "]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.ya = YamlUtil()

    def arrange_teacher(self):
        '''安排考务老师'''
        self.arrange_invigilation()
        self.arrrange_marking()
        self.arrange_inspector()
        self.web.wait(2)
        self.web.click(*self.save)

    def arrange_invigilation(self):
        '''安排监考老师',默认一个考点2个老师，使用自动分配组长'''
        self.web.click(*self.invigilation_area)
        self.web.click(*self.name_tab)
        self.choose_invigi(self.ya.read_extract_yaml('invigilation_num'))
        ele = self.web.find_ele(*self.invigilation_last_id)
        id_text = ele.get_attribute('text')
        self.ya.write_inter_yaml('invigilation_id',id_text)
        self.web.click(*self.auto)
        self.web.click(*self.enter_js)

    def arrrange_marking(self):
        '''安排阅卷老师'''
        self.web.click(*self.marking_teacher)
        self.web.click(*self.marking_area)
        num = int(self.ya.read_extract_yaml('marking_num')) + 1
        self.choose_invigi(num)
        id_text = self.web.find_ele(*self.marking_last_id).get_attribute('text')
        self.ya.write_inter_yaml('marking_id',id_text)
        self.web.click(*self.auto)
        self.web.click(*self.enter_js)

    def arrange_inspector(self):
        '''安排巡考老师'''
        self.web.click(*self.inspector_teacher)
        self.web.click(*self.inspector_area)
        self.choose_invigi()
        self.web.click(*self.auto)
        self.web.click(*self.enter_js)

    def choose_invigi(self,num=2):
        '''
        查找对应得复合元素后，直接操作
        :param num: 默认为2个
        :return:
        '''
        num = int('-' + str(num))
        self.web.wait(2)
        eles = self.web.find_eles(*self.invit_teachers)
        self.web.wait(2)
        for i in eles[num::]:
            i.click()



