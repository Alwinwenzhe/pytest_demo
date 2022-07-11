import pytest


# test_fixture1.py


@pytest.fixture(scope='module', autouse=True)
def test1():
    print('\n开始执行module')


@pytest.fixture(scope='class', autouse=True)
def test2():
    print('\n开始执行class')


@pytest.fixture(scope='function', autouse=True)
def test3():
    print('\n开始执行function')


def test_a():
    print('---用例a执行---')


def test_d():
    print('---用例d执行---')


class TestCase:

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')


if __name__ == '__main__':
    pytest.main(['-s', 'demo_005.py'])