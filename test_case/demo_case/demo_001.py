# -- coding:utf-8 --
import time

import pytest

@pytest.fixture(scope='function',params=['成龙','甄子丹','周杰伦'],ids=['one','two','three'])
def my_fixture(request):            # 这里得request自动接受params得传值，参数request是固定写法
    # 两种传参模式
    # print('\n前置')
    # yield time.time()
    # print('\n后置')
    return request.param           # 注意这里不是params，固定写法

class TestMas1:

    def test_01_baili(self):
        print('\n输出百里')

    @pytest.mark.demo
    def test_02_jialuo(self,my_fixture):    # 这里是接受request.param 返回得值
        print('----------' + str(my_fixture))

if __name__ == '__main__':
    pytest.main(['./demo_001.py'])