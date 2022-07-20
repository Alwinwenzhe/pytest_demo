这个工程是pytest框架学习的汇总，包含了接口
web自动化的相关实现

## Web_case 运行日志
### 07-07 运行无法启动
可以运行了，但是pytest.ini中多线程配置对web自动化没有意义，毕竟是需要焦点
进行输入，所以命令从：
addopts = -vs -reruns=1 -n=2 --alluredir ./temp --dist=loadfile
修改为,去掉了多线程设置，及配置文件加载方式
addopts = -vs -reruns=1 --alluredir ./temp

### 07-07  find_element 没有By.XPATH
错误写法：By.Xpath
正确写法：By.XPATH

ok web_case中的xijiao用例可以正常运行，接下来就是框架优化了

### 07-08 
登录用例手动执行没问题,直接执行,不能输入用户名

### 07-10
将log放入了conftest中，添加了session传递

### 07-20
创建流程已经到第八步，点击'按姓名’时报错
