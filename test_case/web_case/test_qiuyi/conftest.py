import pytest

@pytest.fixture(scope='module',autouse=True)
def log():
    '''实现登录'''

