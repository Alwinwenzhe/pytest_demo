import time

import pytest


@pytest.fixture(scope='session',autouse=True)
def init_connect():
    '''会话之前初始化diriver'''
    print('会话之前初始化连接--pass')
    yield time.time()           # 将time.time()作为参数传递给调用参数，作为一个形式参数，传入函数内部
    print('会话之后关闭连接--pass')

