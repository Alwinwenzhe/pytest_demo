# -- coding:utf-8 --
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("http://www.baidu.com")
t = d.find_element(By.XPATH,"//span[@class='title-content-title']").get_attribute('text')

if __name__ == '__main__':

    print(t)
