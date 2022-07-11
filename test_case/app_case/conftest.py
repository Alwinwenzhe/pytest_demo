import pytest


@pytest.fixture(scope='module',autouse=True)
def init_driver():
    '''会话之前初始化diriver'''
    print('会话之前初始化app_server')

@pytest.fixture(scope='module',autouse=True)
def quit_driver():
    '''会话之前初始化diriver'''
    print('会话之后关闭app_server')