import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


dr = webdriver.Chrome()
dr.get("http://news.baidu.com/")
eles = dr.find_elements(By.XPATH,'//ul[@class="ulist.focuslistnews"]')
print(eles)
