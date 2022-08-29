# -*- coding:utf-8 -*-
# Status:
# Time:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dongchedi.com/")
sel = Select(driver.find_element(By.XPATH,'//input[@placeholder="选择品牌/车系"]'))
sel.deselect_by_value()     # 通过下拉选项的value值选择
sel.deselect_by_index()     # 通过下拉选项的index进行选择
sel.deselect_by_visible_text()      # 通过下拉选项的可见文本进行选择

driver.switch_to.default_content()

