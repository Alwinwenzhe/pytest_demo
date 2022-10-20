import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
寻找考务老师身份证号码
'''

driver = webdriver.Chrome()
driver.get("http://192.168.6.167:3000/teachEvaluation/#/login?redirect=%2Fdashboard")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"userName").clear()
driver.find_element(By.NAME,"userName").send_keys('admin')
driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"password").send_keys('123456')
driver.find_element(By.CLASS_NAME,'el-button.el-button--default.el-button--medium').click()
time.sleep(2)
driver.get('http://192.168.6.167:3000/teachEvaluation/#/plan/teacher?params=%257B%2522isShow%2522%253Afalse%252C%2522newFlag%2522%253Afalse%252C%2522state%2522%253A9%252C%2522subject%2522%253A1%252C%2522planId%2522%253A2248%252C%2522roundNum%2522%253A1%252C%2522generateRound%2522%253A2%252C%2522teacherType%2522%253A3%252C%2522isShowBtn%2522%253Atrue%252C%2522isAiView%2522%253Atrue%252C%2522allowEdit%2522%253A1%252C%2522planCreateType%2522%253A%2522CITY%2522%252C%2522organizationId%2522%253A1000%252C%2522viewMode%2522%253A%2522%25E8%2580%2583%25E5%2590%258E%25E8%25AF%2584%25E5%2588%2586%2522%252C%2522siteRoomNum%2522%253A1%252C%2522invigilationAutoTask%2522%253A1%252C%2522gradeAutoTask%2522%253A1%252C%2522inspectAutoTask%2522%253A1%252C%2522viewCount%2522%253A1%252C%2522arrangeGradeTeacher%2522%253A1%257D')
time.sleep(1)
id = driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
print(id)
time.sleep(3)

