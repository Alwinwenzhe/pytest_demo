# -- coding:utf-8 --
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("http://www.baidu.com")
d.find_element(By.ID,'su').get_attribute('text')

