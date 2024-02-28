# -*- coding:utf-8 -*-
# Status: PASS
# Time:   2022-09-01

import time,random,threading
from common.voice import Voice
from selenium import webdriver
from selenium.webdriver.common.by import By

stu_info = [
        {
           'id': '513401200004073010',
           'name': '杨家兴',
           'mobile': '18582706275',
           'pwd': 'lp@_ZH_123'
       },
         {
            'id': '51342719980301164X',
            'name': '阿鲁莫衣各',
            'mobile': '15237290130',
            'pwd': 'lp@_ZH_123'
        }]

class LPBaoMing(object):

    old_list = ['==请选择==', '木里县', '德昌县', '会东县', '普格县', '布拖县', '金阳县', '昭觉县', '喜德县', '越西县', '甘洛县', '美姑县']

    def __init__(self):
        self.d = webdriver.Chrome()
        self.d.get("http://www.lszzkb.com/SCCZ/Default.aspx")
        # self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.v = Voice()
        self.xichang = (By.XPATH,'//option[@value="2101"]')
        self.ningnan = (By.XPATH,'//option[@value="2107"]')
        self.go_to_loca()

    def go_to_loca(self):
        '''进入位置界面'''
        self.d.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_divlogin"]/table/tbody/tr/td[2]/a/img').click()
        self.d.find_element(By.NAME,'ctl00$ContentPlaceHolder1$btnConfirm').click()
        self.d.find_element(By.NAME,'ctl00$ContentPlaceHolder1$btnConfirm').click()

    def detection_loca(self,j):
        '''每隔30s检测一次西昌市及汉源是否有位置'''
        flag = True
        while flag:
            self.d.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$DDLXqdm').click()
            sum_options = self.d.find_elements(By.XPATH, '//select[@id="ctl00_ContentPlaceHolder1_DDLXqdm"]/option')
            new_list = []
            for i in sum_options:
                text = i.get_attribute('text')
                new_list.append(text)
            if new_list.__len__() != self.old_list.__len__():
                if j ==0 and '西昌市' in new_list:
                    print("\033[0;31;40m", '西昌位置放出来了'  + time.ctime(), "\033[0m" )
                    self.sign_up('xichang',j)
                    for i in range(5):
                        self.v.machine_read("亲爱的宝宝：李佩，请注意：凉山州的西昌市已经放位置出来了")
                        time.sleep(10)
                    user_input = input('用户输入以使程序暂停：')
                elif j ==1 and '宁南县' in new_list:
                    print("\033[0;31;40m", "宁南县放出来了" + time.ctime(), "\033[0m")
                    self.sign_up('ningnan',j)
                    for i in range(5):
                        self.v.machine_read("亲爱的宝宝：李佩，请注意：凉山州的宁南县已经放位置出来了")
                        time.sleep(10)
                    user_input = input('用户输入以使程序暂停：')
                # print('尝试第' + str(j) + "次，没有发现放出来>>>>>>>>>>>>>>>>>")
            wait = 20 + random.randint(0, 30)
            time.sleep(wait)
            self.d.refresh()

    def sign_up(self,city,j):
        '''
        进行报名操作
        :param city: 报名区县
        :param j: 传递list得index
        :return:
        '''
        if city == 'xichang':
            key = 'stu_xichang'
            ele = (By.XPATH,'//option[@value="2101"]')
        elif city == 'ningnan':
            key = 'stu_ningnan'
            ele = (By.XPATH, '//option[@value="2107"]')
        else:
            self.v.machine_read('区县信息错误')

        self.d.find_element(*ele).click()
        # 操作报名点

        self.d.find_element(By.ID,'ctl00_ContentPlaceHolder1_DDLBmd').click()
        time.sleep(1)
        self.d.find_element(By.XPATH,'//select[@id="ctl00_ContentPlaceHolder1_DDLBmd"]/option[2]').click()
        # 输入身份证等
        self.d.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TBUser').send_keys(stu_info[j]['id'])
        self.d.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TBName').send_keys(stu_info[j]['name'])
        self.d.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbPhone').send_keys(stu_info[j]['mobile'])
        self.d.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TBPassWord').send_keys(stu_info[j]['pwd'])
        self.d.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TBRePassword').send_keys(stu_info[j]['pwd'])
        # 图片验证码

    def test(self,x, y):
        for i in range(x, y):
            print(i)

if __name__ == '__main__':
    '''多线程启动检测并自动填入信息'''
    thread_list = []
    for i in range(len(stu_info)):
        b = LPBaoMing()
        i =  threading.Thread(name='t1',target=b.detection_loca,args=(i,))
        thread_list.append(i)
    for i in thread_list:
        i.start()
        print('启动成功：', i)

