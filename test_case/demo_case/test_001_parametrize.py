import os

import pytest, requests, allure
from common.yaml_util import YamlUtil

@pytest.fixture(scope='function')
def execute_database_sql():
    print('数据库前置查询')        # 这里是前置
    yield                           # 这里开始就是后置
    print('关闭数据库连接')

class Test001Parametrize:

    # @pytest.mark.smoke
    @pytest.mark.parametrize('name,age',[['佩佩',18],['函数',5]])
    def test_01_para(self,name,age):
        print(name,age)

    @pytest.mark.smoke
    def test_02_inter(self):
        '''一生约隐私协议'''
        url = 'https://api.yishengyue.cn/api/v1/user/getUserPrivacyPolicy?mobile=15828022852'
        header = {
            'Content-Type': 'application/json; charset=UTF-8',
            'enterpriseId': '1122c78ae5d140a5acbaa9e75c8b8994',
            'accessToken': '41C161B87DA6BF3349F88F490869A699A339AC6BD2A711E06962565F77D3EB398C270C0BCE5F9663F487347F2C61CC0DB1E8FE298603511744188F6A61A923F9'
        }
        res = requests.get(url)
        assert 'code":0' in res.text


    @pytest.mark.smoke
    def test_03_house_list(self):
        '''一生约15828022852获取房屋列表'''
        url = 'https://api.yishengyue.cn/api/v1/family/house/list?userId=0f5cfb3b94af4ab2a8c7c52c81053b8a'
        header = {
            'Content-Type':'application/json; charset=UTF-8',
            'enterpriseId':'1122c78ae5d140a5acbaa9e75c8b8994',
            'accessToken':'41C161B87DA6BF3349F88F490869A699A339AC6BD2A711E06962565F77D3EB398C270C0BCE5F9663F487347F2C61CC0DB1E8FE298603511744188F6A61A923F9'
        }
        res = requests.get(url=url,headers=header)
        assert 'code":0' in res.text

    # 已经被 test_ysy_002_health_data.py 替代
    # @pytest.mark.demo
    # @pytest.mark.parametrize('case',YamlUtil().read_inter_yaml())
    # def test_04_yaml_add_step(self,case,execute_database_sql):      # execute_database_sql 引用前后置
    #     '''数据来源于yaml文件'''
    #     print(case)
    #     url = case['request']['url']
    #     header = case['request']['headers']
    #     data = case['request']['params']
    #     assert_info = case['validate']['in']
    #     res = requests.post(url=url, headers=header, json=data)
    #     assert 'code":0' in res.text



if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(root_path)