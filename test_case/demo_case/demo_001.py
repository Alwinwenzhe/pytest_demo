import pytest


# 定义fixture，每次调用时返回一个新的值
@pytest.fixture(scope="function")  # scope设置为function表示每个测试方法都会有一个新的fixture实例
def my_value():
    value = 0  # 初始值
    yield value  # 返回当前值给测试方法
    # 这里可以放置清理逻辑，但在这个例子中我们不需要


class TestMyValues:

    def test_increment_value(self, my_value):
        # 使用fixture提供的初始值
        assert my_value == 0
        my_value += 1  # 修改fixture返回的值（但这不会影响下一个测试方法中的fixture值）
        assert my_value == 1

    def test_another_method_with_value(self, my_value):
        # 在这个测试方法中，我们又得到了fixture的初始值，因为它是一个新的实例
        assert my_value == 0
        # 在这里可以对值进行其他操作
