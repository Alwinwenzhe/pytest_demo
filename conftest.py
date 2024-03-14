import time, os, glob
import pytest


@pytest.fixture(scope='session', autouse=True)
def init_connect():
    '''会话之前初始化diriver'''
    print('会话之前初始化连接--pass')
    yield time.time()  # 将time.time()作为参数传递给调用参数，作为一个形式参数，传入函数内部
    print('会话之后关闭连接--pass')
    pytest_sessionfinish()


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


def delete_json_files(directory):
    """删除指定目录下的所有JSON文件"""
    json_files = glob.glob(os.path.join(directory, '*.json'))
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    files = json_files + txt_files
    for i in files:
        try:
            os.remove(i)
            print(f"Deleted JSON file: {i}")
        except OSError as e:
            print(f"Error: {e.strerror} : {i}")


def pytest_sessionfinish(session, exitstatus):
    """pytest会话结束时调用的钩子函数"""
    # 假设你的JSON文件都存放在'results'目录下
    results_dir = './tmp'  # 根据实际情况修改这个路径
    delete_json_files(results_dir)
