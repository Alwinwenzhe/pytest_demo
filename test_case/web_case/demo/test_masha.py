# -- coding:utf-8 --

class TestMas:

    # 这个在所有用例之前之前执行一次
    def setup_class(self):
        print("在每个类执行前得初始化工作，比如：创建日志对象，数据库连接")

    # 在每个用例之前执行一次
    def setup(self):
        print("\n在执行测试用例之前初始化得代码：打开浏览器，加载网页")

    def test_01_baili(self):
        print("\n输出百里")

    def test_02_jialuo(self):
        print("\n输出伽罗")

    def teardown(self):
        print("\n在执行测试用例之后得扫尾工作：关闭浏览器")

    def teardown_class(self):
        print("\n在每个类执行后得扫尾工作，比如：销毁日志对象，销毁数据库连接")