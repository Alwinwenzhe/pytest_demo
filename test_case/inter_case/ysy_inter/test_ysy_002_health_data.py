# -- coding:utf-8 --
# Comment：通过yaml管理测试用例
# Status:pass
import allure
import pytest
from common.asert import Asert
from common.yaml_util import YamlUtil
from common.all_request import AllRequest
from common.my_log import MyLog

@allure.feature('健康模块')
class TestYsy002HealthData:

    #pytest中就没有构建函数__init__

    age = 20
    asert = Asert()
    mylog = MyLog()
    sess = AllRequest().session

    @pytest.mark.skipif(age>=18,reason='已成年')
    def test_002_skipif(self):
        print('this is a intercase 005!')

    @allure.story('获取家庭成员标签')
    @allure.step('获取家庭成员标签')
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize('case', YamlUtil().read_inter_yaml(r'/test_case/inter_case/test_ysy_002_get_member_tag.yaml'))
    def test_003_get_member_tag(self,case):
        url = case['request']['url'] + str(YamlUtil().read_yaml('userId'))
        header = case['request']['headers']
        request_method = case['request']['method']
        header['accessToken'] = YamlUtil().read_yaml('accessToken')
        assert_info = case['validate']
        # res = requests.request(request_method,url=url, headers=header)
        res = self.sess.request(request_method,url=url, headers=header)
        self.asert.assert_yaml(assert_info, res.text, self.mylog)  # res.text 响应内容是文本格式，另外还有json格式


    # @allure.story('添加步数')
    # @allure.step('添加步数')
    # @pytest.mark.run(order=1)
    # @pytest.mark.skipif(age>40,reason='年龄太大，不适应上班')
    # @pytest.mark.demo
    # @pytest.mark.parametrize('case',YamlUtil().read_instead_yaml('./test_case/inter_case/add_step.csv','./test_case/inter_case/test_ysy_002_add_step.yaml'))
    # def test_004_yaml_add_step(self,case,get_token):      # execute_database_sql 引用前后置
    #     '''注意：这里得token是通过conftest配置文件获取'''
    #     url = case['request']['url']
    #     case['request']['headers']['accessToken'] = get_token
    #     request_method = case['request']['method']
    #     header = case['request']['headers']
    #     data = case['request']['params']
    #     assert_info = case['validate'][1]
    #     self.mylog.info('正在执行用例：'+ case['name'])
    #     res = self.sess.request(request_method,url=url, headers=header, json=data)   # 当使用json=data，那么等同于header中写入了：Content-Type: application/json; charset=UTF-8
    #     # 这里还缺少一步，如果用例执行成功后，需要写入全局变量：extract.yaml
    #     self.asert.assert_yaml(assert_info,res.text,self.mylog)     # res.text 响应内容是文本格式，另外还有json格式

    # # @pytest.mark.skip('只是随便找个接口尝试一下上传文件')
    # @allure.step('上传文件demo')
    # @pytest.mark.demo
    # @pytest.mark.parametrize('case', YamlUtil().read_instead_yaml('./test_case/inter_case/add_step.csv', './test_case/inter_case/test_ysy_002_add_step.yaml'))
    # def test_005_upload_file(self,case,get_token):
    #         '''注意：这里得token是通过conftest配置文件获取'''
    #         url = case['request']['url']
    #         case['request']['headers']['accessToken'] = get_token
    #         request_method = case['request']['method']
    #         header = case['request']['headers']
    #         data = case['request']['params']
    #         assert_info = case['validate'][1]
    #         self.mylog.info('正在执行用例：' + case['name'])
    #         file_word = open(r'D:\job\pic\人脸\李艳平2.png',mode='rb')   # 二进制方式读取文件,这个接口是强行传递
    #         res = self.sess.request(request_method, url=url, headers=header,
    #                                 json=data,files=file_word)  # 当使用json=data，那么等同于header中写入了：Content-Type: application/json; charset=UTF-8
    #         # 这里还缺少一步，如果用例执行成功后，需要写入全局变量：extract.yaml
    #         self.asert.assert_yaml(assert_info, res.text, self.mylog)  # res.text 响应内容是文本格式，另外还有json格式
