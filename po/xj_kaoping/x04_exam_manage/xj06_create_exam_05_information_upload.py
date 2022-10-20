# -*- coding:utf-8 -*-
# Status:
# Time:
from common.win import win_upload
from common.web_common.web_key import WebKey
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.deal_time import DealTime

class Xj06CreateExam05InformationUpload(object):

    url = 'http://192.168.6.167:3000/teachEvaluation/#/plan/planAdd'

    # 批量导入学生
    import_student = (By.XPATH,'//span[text()="批量导入学生"]')
    # 上传学生数据
    upload_stu_data = (By.CLASS_NAME,'siteBox')
    # 点击上传区域
    upload_area = (By.CLASS_NAME,'el-upload__text')
    # 确定
    stu_enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[1].click()"
    # 弹窗确定
    stu_alert_enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[2].click()"
    # 返回
    retur = (By.XPATH,"//span[text()='返回']")

    # 批量导入教师
    upload_teacher = (By.XPATH,"//span[text()='批量导入教师']")
    #   监考
    #   监考老师上传区域
    invigilation_area = (By.CLASS_NAME,"iconfont.build.icon-a-2413")
    #   点击或拖动上传
    invigilation_file_upload = (By.CLASS_NAME,"iconfont.icon-shangchuan")
    #   确定 通过某节点的父亲，再定位父亲的弟弟
    # enter = (By.XPATH,"//span[text()='取消']/../following-sibling::div[1]")
    enter_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[3].click()"
    alert_js = "document.getElementsByClassName('el-button el-button--primary el-button--medium')[4].click()"
    cancel = (By.XPATH, '//span[text()="取消"]')

    #   阅卷老师
    marking_teacher = (By.ID,'tab-reviewTeacher')
    #   阅卷老师上传区域
    marking_area = (By.XPATH,'//span[text()="点击上传阅卷老师数据"]')
    #   点击或拖动上传--同上：invigilation_file_upload

    #   巡考老师
    inspector_teacher = (By.ID,'tab-inspectorTeacher')
    #   巡考老师区域
    inspector_area = (By.XPATH,'//span[text()="点击上传巡考老师数据"]')
    #   点击拖动上传/确定/取消都同上


    # 下一步选择考点
    next = (By.XPATH,'//span[contains(text(),"保存并开始下一步选择考点")]')

    def __init__(self,driver):
        self.web = WebKey(driver)
        self.tim = DealTime()

    def upload(self):
        '''上传信息'''
        self.upload_student()
        # 批量导入教师
        self.web.click(*self.upload_teacher)
        self.upload_invigilation()
        self.upload_marking()
        self.upload_inspector()
        # 返回并下一步
        self.web.click(*self.retur)
        self.web.click(*self.next)


    def upload_student(self):
        # 上传学生
        self.web.click(*self.import_student)
        self.web.click(*self.upload_stu_data)
        self.web.click(*self.upload_area)
        self.web.wait(1)
        win_upload(r'J:\now_job\西交智汇\data\学校\AT_高新-3\成都七中\学生_6.xlsx')
        self.web.wait(3)
        self.web.exec_js(self.stu_enter_js)
        self.web.exec_js(self.stu_alert_enter_js)
        self.web.wait(3)
        self.web.click(*self.retur)

    def upload_invigilation(self):
        #   上传监考教师
        self.web.click(*self.invigilation_area)
        self.web.click(*self.invigilation_file_upload)
        self.web.wait(2)
        win_upload(r'J:\now_job\西交智汇\data\学校\AT_高新-3\成都七中\监考老师.xlsx')
        self.web.wait(3)
        self.web.exec_js(self.enter_js)
        self.web.wait(1)
        self.web.exec_js(self.alert_js)
        self.web.click(*self.cancel)

    def upload_marking(self):
        #   上传阅卷老师
        self.web.click(*self.marking_teacher)
        self.web.click(*self.marking_area)
        self.web.click(*self.invigilation_file_upload)
        self.web.wait(2)
        win_upload(r'J:\now_job\西交智汇\data\学校\AT_高新-3\成都七中\阅卷老师.xlsx')
        self.web.wait(3)
        self.web.exec_js(self.enter_js)
        self.web.exec_js(self.alert_js)
        self.web.click(*self.cancel)

    def upload_inspector(self):
        #   上传巡考考试
        self.web.click(*self.inspector_teacher)
        self.web.click(*self.inspector_area)
        self.web.click(*self.invigilation_file_upload)
        self.web.wait(2)
        win_upload(r'J:\now_job\西交智汇\data\学校\AT_高新-3\成都七中\巡考老师.xlsx')
        self.web.wait(3)
        self.web.exec_js(self.enter_js)
        self.web.exec_js(self.alert_js)
        self.web.click(*self.cancel)









