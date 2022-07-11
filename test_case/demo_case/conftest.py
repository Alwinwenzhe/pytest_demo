import pytest


@pytest.fixture(scope='module',autouse=True)
def init_class():
    print('''demo运行前init''')