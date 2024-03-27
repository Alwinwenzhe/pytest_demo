from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# 使用 webdriver-manager 来自动下载和管理 GeckoDriver
# 这样可以避免手动下载和配置 GeckoDriver
service = Service(GeckoDriverManager().install())

# 初始化 Firefox WebDriver
driver = webdriver.Firefox(service=service)
driver.maximize_window()

# 打开百度主页
driver.get("https://www.baidu.com")

# 查找搜索框
search_box = driver.find_element(By.ID, "kw")

# 在搜索框中输入搜索内容，例如 "Selenium"
search_box.send_keys("Selenium")

# 执行搜索
search_box.send_keys(Keys.RETURN)

# 等待搜索结果加载（可选，根据实际情况调整）
# driver.implicitly_wait(10)

# 打印页面标题来确认搜索成功
print(driver.title)

# # 关闭浏览器
# driver.quit()
