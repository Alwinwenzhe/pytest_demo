import allure
import pytest

@allure.feature('这里是一级标签')
class TestAllure():

    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    @pytest.mark.parametrize('param', ['青铜', '白银', '黄金'])
    def test_0(self, param):
        allure.attach('附件内容是： '+param, '我是附件名', allure.attachment_type.TEXT)

    @allure.title("用例标题1")
    @allure.story("这里是第二个二级标签")
    def test_1(self):
        allure.attach.file(r'J:\now_job\pic\face\li.png', '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)

    @allure.title("用例标题2")
    @allure.story("这里是第三个二级标签")
    @allure.issue('http://baidu.com', name='点击我跳转百度')
    @allure.testcase('hhttp://192.168.6.167:3000/teachEvaluation/#/dashboard', name='点击我跳转考评')
    def test_2(self):
        pass

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])