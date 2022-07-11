# -- coding:utf-8 --
import pytest

@pytest.fixture(scope='function',params=['成龙','甄子丹','周杰伦'])
def my_fixture(request):            # 这里得request自动接受params得传值
    print('前置')
    yield
    print('后置')
    return request.param            # 注意这里不是params，固定写法

class TestMas1:

    def test_01_baili(self):
        print('\n输出百里')

    def test_02_jialuo(self,my_fixture):    # 这里是接受request.param 返回得值
        print('\n输出伽罗')
        print('----------' + str(my_fixture))