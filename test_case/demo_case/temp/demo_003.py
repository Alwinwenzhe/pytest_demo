import os

import pytest, requests
from common.yaml_util import YamlUtil


@pytest.fixture(scope='function')
def execute_database_sql():
    print('数据库前置查询')  # 这里是前置
    yield  # 这里开始就是后置
    print('关闭数据库连接')




class Test001Parametrize:

    @pytest.mark.demo
    @pytest.mark.parametrize('case', YamlUtil().read_inter_yaml())
    def test_04_yaml_add_step(self, case, execute_database_sql):  # execute_database_sql 引用前后置
        '''数据来源于yaml文件'''
        print(case)
        url = case['request']['url']
        header = case['request']['headers']
        data = case['request']['params']
        assert_info = case['validate']['in']
        res = requests.post(url=url, headers=header, json=data)
        assert 'code":0' in res.text


if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(root_path)