# -*- coding:utf-8 -*-
import yaml, os

class WriteUserCommand(object):

    def __init__(self):
        # parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))   # 返回上一级目录
        self.root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # self.user_info_dir = (parent_dir + '/config.yaml').replace('\\', '/')
        self.devices_info = (self.root_path + '/test_case/app_case/devices.yaml')

    def readyaml(self):
        '''
        读取yaml文件
        :return:
        '''
        with open(self.devices_info,'r') as f:
            data = yaml.load(f,Loader=yaml.FullLoader)
        return data

    def write_yaml(self,i,b_port,bp_port,devices_name):
        '''
        写入yaml
        :return:
        '''
        self.clear_user_info()
        data = self.join_data(i,b_port,bp_port,devices_name)
        with open(self.devices_info,'a') as f:        # a--追加
            yaml.dump(data,f)

    def join_data(self,i,b_port,bp_port,devices_name):
        '''
        拼接数据
        :param i:
        :param b_port:
        :param bp_port:
        :param devices_name:
        :return:
        '''
        data = {
        "user_info_" + str(i): {
        "b":b_port,
        "bp":bp_port,
        "devicesname":devices_name
        }
        }
        return data

    def clear_user_info(self):
        '''
        运行前清理user_info
        :return:
        '''

        with open(self.devices_info,'w') as f:
            f.truncate()

    def get_yaml(self,key1,key2,*args):
        '''
        从yaml获取指定设备及其信息
        :param key:
        :param value:
        :return:
        '''
        return self.readyaml()[key1][key2]

    def get_count(self):
        '''获取数据长度'''
        try:        # 检测可能出错的代码
            data = self.readyaml()
            if data == None:        # 主动出发异常
                raise ValueError("请检查是否有手机连接".center(60,'>'))
        except ValueError as e:
            print(e)
        else:           #  如果没有异常执行该代码
            len = data.__len__()
            return len

if __name__ == '__main__':
    wu = WriteUserCommand()
    print(wu.root_path)
    print(wu.readyaml())
    print(wu.write_yaml(5,4701,4901,12344))
    print(wu.readyaml())
    print(wu.get_yaml('user_info_5')['b'])