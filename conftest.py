import time, os

import pytest


@pytest.fixture(scope='session',autouse=True)
def init_connect():
    '''会话之前初始化diriver'''
    print('会话之前初始化连接--pass')
    yield time.time()           # 将time.time()作为参数传递给调用参数，作为一个形式参数，传入函数内部
    print('会话之后关闭连接--pass')


def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="debug",
                     help="当前三个环境 : debug or dev or test")


# @pytest.fixture(scope="session")
# def env(request):
#     print("\nCurrent env is : %s" % request.config.getoption("--environment"))
#     config = os.path.join(config_path, request.config.getoption("--environment"), "config.yaml")
#     with open(config, "r", encoding="utf-8") as f:
#         env_config = yaml.safe_load(f)
#     return env_config