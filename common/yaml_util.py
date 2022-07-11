import os
import yaml
from common import deal_csv
from contextlib import ExitStack
from common import deal_csv

class YamlUtil:

    def __init__(self):
        self.root_path = os.path.dirname(os.path.dirname(__file__))
        self.file_path = self.root_path + '/data'


    # def read_config_yaml(self,one_name,two_name):
    #     '''读取全局配置yaml文件'''
    #     with open(self.file_path + '/config.yaml',mode='r',encoding='utf-8') as f:
    #         value = yaml.load(f.read(),Loader=yaml.FullLoader)
    #         return value

    def read_extract_yaml(self,key):
        '''读取临时存放数据得yaml文件'''
        with open(self.root_path + '/extract.yaml',encoding='utf-8') as  f:
            value = yaml.load(f.read(),Loader=yaml.FullLoader)
            return value[key]

    def read_inter_yaml(self,file_name):
        '''
        读取yaml,对yaml反序列化(yaml格式转化为dict)
        :return:
        '''
        with open(self.root_path + file_name,mode='r',encoding='utf-8') as f:
            value = yaml.load(f.read(),Loader=yaml.FullLoader)
            return value

    def read_instead_yaml(self,case_list,file_name):
        '''csv遍历生成用例后，返回真正得用例集'''
        self.clear_yaml(r'/test_case/inter_case/cases.yaml')
        cases = deal_csv.FromCsvToJson(case_list)
        self.env_raplace_yaml(cases,file_name)
        return self.read_inter_yaml(r'/test_case/inter_case/cases.yaml')

    def write_inter_yaml(self,write_dict_data,file_name):
        '''写入yaml'''
        with open(self.root_path + file_name,mode='a', encoding='utf-8') as f:
            yaml.dump(write_dict_data,f)

    def clear_yaml(self,file_name):
        '''清空yaml'''
        with open(self.root_path + file_name, mode='w', encoding='utf-8') as f:
            f.truncate()

    def read_config_file(self,node):
        '''读取根目录config中得值'''
        with open(self.root_path + r'\\config.yaml', mode='r', encoding='utf-8') as f:
            value = yaml.load(f.read(),Loader=yaml.FullLoader)
            return value[node]

    def env_raplace_yaml(self,case_list,yaml_file):
        '''
        调试通过 看看细节
        :param yaml_file: 为YAML模板文件
        :param new_yaml_file: 为新生成的带有测试数据的YAML文件
        :return:

        '''
        new_yaml_file = self.root_path + r'/test_case/inter_case/cases.yaml'
        try:
            with ExitStack() as stack:
                yml_file = stack.enter_context(open(yaml_file, 'r+'))
                yml_output = stack.enter_context(open(new_yaml_file, 'w'))
                # 先读取YAML模板文件，返回值为字符串列表
                yml_file_lines = yml_file.readlines()
                # profileList的长度即为测试用例的数量
                for i in range(0, len(case_list)):
                    # 循环遍历列表
                    for line in yml_file_lines:
                        new_line = line
                        # 如果找到以“$csv{”开头的字符串
                        if new_line.find('$csv{') > 0:
                            # 对字符串以“:”切割
                            env_list = new_line.split(':')
                            # 取“:”后面的部分，去掉首尾空格，再以“{”切割，再以“}”切割取出变量名称，比如“name”
                            env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]
                            replacement = ""
                            # 如果name在字典列表的key里
                            if env_name in case_list[i].keys():
                                # 取出name对应的值赋给replacement
                                replacement = case_list[i][env_name]
                                # 用replacement替换掉YAML模板中的“$csv{name}”
                                for j in range(0, len(case_list)):
                                    new_line = new_line.replace(env_list[1].strip(), replacement)
                        # 将new_line写入到yml_output文件里
                        yml_output.write(new_line)
                    yml_output.write("\n")
        except IOError as e:
            print("Error: " + format(str(e)))
            raise



if __name__ == '__main__':
    yal = YamlUtil()
    old_file = yal.root_path + r'/test_case/inter_case/test_ysy_002_add_step.yaml'
    add_step_cases = deal_csv.FromCsvToJson(yal.root_path + '/test_case/inter_case/add_step.csv')
    yal.env_raplace_yaml(add_step_cases,old_file)