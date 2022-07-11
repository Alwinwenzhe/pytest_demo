import time

import pytest
from common import yaml_util

yam = yaml_util.YamlUtil()

@pytest.fixture(scope='module',autouse=True)
def init_db():
    '''会话之前初始化diriver'''
    print('模块级别前置初始化db--pass')
    yield time.time()
    print('模块级别后置结束关闭db--pass')

@pytest.fixture(autouse=True)   # 修改为默认每个函数生效，避免token更新了还不知道
def get_token():            # 这里得request自动接受params得传值，参数request是固定写法
    '''
    每个py文件运行前获取token，如果是执行登录用例需要直接替换为最新的token，这里占时未实现
    :return:
    '''
    return yam.read_extract_yaml('accessToken')

if __name__ == '__main__':
    print(get_token())



