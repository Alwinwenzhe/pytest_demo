# -- coding:utf-8 --
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import random

class WebKey:

    def __init__(self,driver):
        '''初始化driver及配置'''
        self.driver = driver
        self.driver.implicitly_wait(10)

    def random_1(self,num=1,*args,**kwargs):
        '''随机1秒内休息,或大于2的随机'''
        if num == 1 :
            rand_sleep = random.randrange(1,3)
            sleep(rand_sleep)
        else:
            sleep(num)

    def exec_js(self,js,*args,**kwargs):
        '''当定位出问题，可以使用js执行'''
        self.driver.execute_script(js)
        self.random_1(5)

    def open(self,txt,*args,**kwargs):
        '''封装get'''
        self.driver.get(txt)
        self.random_1()

    def get_cur_url(self,*args,**kwargs):
        '''获取当前url'''
        return self.driver.current_url

    def refresh(self):
        '''刷新'''
        self.driver.refresh()
        self.random_1()

    def find_ele(self,by,value,timeout=10, poll=0.5,*args,**kwargs):
        """
        自定义一个元素查找方法
        依据用户传入的元素信息特征，然后返回当前用户想要查找元素
        :param feature: 元组类型，包含用户希望的查找方式，及该方式对应的值
        :return: 返回当前用户查找的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by,value))
            return ele
        except Exception as e:
            print(e)
        # finally:
        #     return ele

    def find_eles(self,by,value,timeout=10, poll=0.5,*args,**kwargs):
        '''
        查找元素,增加了try except
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:  返回的list从0开始
        '''
        try:
            eles = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by,value))
            return eles
        except Exception as e:
            print(e)


    def click(self,by,value):
        '''
        点击元素
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:
        '''
        self.find_ele(by,value).click()

    def move_to_ele_and_click(self,driver,ele1,ele2,*args,**kwargs):
       '''
       移动鼠标到某个元素，并点击
       :param driver:
       :param ele1: 移动到这个元素
       :param by: 点击元素的by方式
       :param value: 点击元素得value值
       :param args:
       :param kwargs:
       :return:
       '''
       el1 = self.find_ele(*ele1)
       ActionChains(driver).move_to_element(el1).perform()
       self.click(*ele2)

    def send(self,by,value,txt,*args,**kwargs):
        '''
        填写内容
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :param content: 填写内容
        :return:
        '''
        self.find_ele(by,value).clear()
        self.find_ele(by,value).send_keys(txt)

    def web_wait(self,by,value,*args,**kwargs):
        '''
        显示等待某个元素
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:
        '''
        self.random_1()
        return WebDriverWait(self.driver,10,0.5).until(
            lambda el:self.find_ele(by,value),message='显示查找元素失败'
        )

    def quit(self):
        '''
        关闭浏览器并删除后台进程
        :return:
        '''
        self.driver.quit()

    def wait(self,time_,*args,**kwargs):
        '''强制等待时间'''
        sleep(int(time_))

    def switch_frame(self,by,value=None,*args,**kwargs):
        '''
        通过id，name，index，webelement定位方法来切换窗口
        :param name:可以是：id，name，index
        :param value: webelement定位方法来识别frame或iframe
        :return:
        '''
        if value==None:
            self.driver.switch_to.frame(by)
        else:
            self.driver.switch_to.frame(self.find_ele(by,value))
        self.random_1()

    def switch_default(self,*args,**kwargs):
        '''切换到默认的frame'''
        self.driver.switch_to.default_content()

    def switch_handle(self,close=False,index=1,*args,**kwargs):
        '''
        通过窗口句柄或窗口名字切换到新窗口
        第一个句柄默认是0，新打开的默认句柄为1
        :return:
        '''
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])
        self.random_1()

    def relative_locator(self,direct,by,value,ele,*args,**kwargs):
        '''
        相对定位,这里写的好像有问题
        :param direct:
        :param by:
        :param value:
        :param ele:
        :return:
        '''
        direction = {
            'up': "above",
            'left': "to_left_of",
            'right': "to_right_of",
            'near': 'near'
        }
        by_method = {
            'id': By.ID,
            'name': By.NAME,
            'class': By.CLASS_NAME,
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'link text': By.LINK_TEXT,
            'part link': By.PARTIAL_LINK_TEXT,
            'tag name': By.TAG_NAME
        }
        return self.driver.find_element(locate_with(by_method[by], value)).direction[direct](ele)

    #other相对定位器
    def locator_with(self,method,value,by,el_value,direction,*args,**kwargs):
        el = self.find_ele(by,el_value)
        direction_dict = {
             'up': "above",
            'left': "to_left_of",
            'right': "to_right_of",
            'near': 'near',
            'below': 'below'
        }
        if isinstance(method,str):
            method_dict = {
                'id': By.ID,
                'name': By.NAME,
                'class': By.CLASS_NAME,
                'css': By.CSS_SELECTOR,
                'xpath': By.XPATH,
                'link text': By.LINK_TEXT,
                'part link': By.PARTIAL_LINK_TEXT,
                'tag name': By.TAG_NAME
            }
        return  self.driver.find_element(getattr(locate_with(method_dict.get(method),value))),direction_dict.get(direction)(el)

    def assert_text(self,by,value,txt,*args,**kwargs):
        '''
        判定执行后，通过识别预期元素判定执行结果
        :param name:
        :param value:
        :param txt:
        :return:
        '''
        try:
            result = self.web_wait(by,value).text
            assert result == txt,'执行失败，预期结果文本是{0},实际执行后得到文本是{1}'.format(txt,result)
            return True
        except Exception as e:
            print("断言信息失败：" + str(e))
            return False
        self.random_1()

    def assert_url(self, expect_url,*args,**kwargs):
        '''
        通过当前url，判断执行是否成功
        '''
        cur_url = self.get_cur_url()
        result = True if cur_url == expect_url else False
        return result


if __name__ == '__main__':
    wk = WebKey()
    wk.random_1(6)
