# Author:
# Data:
# Status
# Comment:excel中请求内容如果是json，那么json内容单独存放在json.json文件中，通过该py文件读取json内容

import os
import json

class OperateJson(object):

    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        self.file_path = self.path_dir + r'\data\temp_data.json'
        #如果构建函数中增加了下行代码会导致用例:第一个用例修改了json，第二个用例读取最新json值会读到旧值；因为初始化就会将json文件读入到内存，的第二次会督导内存中的值
        # self.json_data = self.read_json()

    def read_json(self,*args,**kwargs):
        """
        读取json文件
        :return:
        """
        with open(self.file_path, 'r', encoding='UTF-8') as fp:
            data = json.load(fp)            # load:把文件打开从字符串转换成数据类型
            return data

    def get_json_value(self, id,*args,**kwargs):
        """
        获取对应json值,这里会读到上一次token信息
        :param id:
        :return:
        """
        data = self.read_json()[id]
        return data

    def write_json_value(self,*args,**kwargs):
        """
        将新值写入json原有数据中，如果值相同，则覆盖
        每次写入一组数据
        :param key:
        :param value:
        :return:
        """
        # 单独读取文件
        init_json = self.read_json()
        for key in kwargs.keys():
            init_json[key] = kwargs[key]
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            json.dump(init_json, f)         # dump把数据类型转换成字符串并存储在文件中


if __name__ == '__main__':
    rj = OperateJson()
    print(rj.path_dir)

