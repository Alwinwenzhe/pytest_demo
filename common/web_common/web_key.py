# -- coding:utf-8 --
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from common.web_common.chrome_option import ChromeOptions


def open_browser(type_='Chrome'):
    '''基于type_值决定生成的driver对象是什么类型'''
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=ChromeOptions().options())
    else:
        try:
            driver = getattr(webdriver,type_)()
        except Exception as e:
            print("Exception Information:",str(e))
            driver = webdriver.Chrome()
    return driver

class WebKey:


    def __init__(self):
        '''初始化driver及配置'''
        self.driver = open_browser()
        self.driver.implicitly_wait(10)

    def open(self,txt):
        '''封装get'''
        self.driver.get(txt)

    def refresh(self):
        '''刷新'''
        self.driver.refresh()

    def find_ele(self,by,value):
        '''
        查找元素
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:
        '''
        return self.driver.find_element(by,value)

    def click(self,by,value):
        '''
        点击元素
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:
        '''
        self.find_ele(by,value).click()

    def send(self,by,value,txt):
        '''
        填写内容
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :param content: 填写内容
        :return:
        '''
        self.find_ele(by,value).clear()
        self.find_ele(by,value).send_keys(txt)

    def web_wait(self,by,value):
        '''
        显示等待某个元素
        :param by:    查找方式，比如：id、name等
        :param value: 该方式对应的元素值
        :return:
        '''
        return WebDriverWait(self.driver,10,0.5).until(
            lambda el:self.find_ele(by,value),message='显示查找元素失败'
        )

    def quit(self):
        '''
        关闭浏览器并删除后台进程
        :return:
        '''
        self.driver.quit()

    def wait(self,time_):
        '''强制等待时间'''
        sleep(int(time_))

    def switch_frame(self,by,value=None):
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

    def switch_default(self):
        '''切换到默认的frame'''
        self.driver.switch_to.default_content()

    def switch_handle(self,close=False,index=1):
        '''
        通过窗口句柄或窗口名字切换到新窗口
        第一个句柄默认是0，新打开的默认句柄为1
        :return:
        '''
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    def relative_locator(self,direct,by,value,ele):
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
    def locator_with(self,method,value,by,el_value,direction):
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

    def assert_text(self,by,value,txt):
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

