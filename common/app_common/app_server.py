# -*- coding:UTF-8 -*-
import os,threading,time
from common.app_common.dos_cmd import DosCmd
from common.app_common.write_user_command import WriteUserCommand


class AppServer(object):

    def __init__(self):
        self.doc = DosCmd()
        self.wu =WriteUserCommand()
        self.dev_list = self.find_devices()

    def find_devices(self):
        '''查找设备数'''
        dev_lists = []
        dev_list = self.doc.cmd_result('adb devices')
        for i in dev_list[1::]:    # 去掉第一个何最后一个空值
            d = i.split('\t')
            dev_lists.append(d[0])
        return dev_lists

    def check_port_used(self,port):
        '''
        检查端口是否被占用
        :param port:
        :return: True--代表未占用
        '''
        cmd_str = "netstat -ano | findstr " + str(port)
        cmd_result = self.doc.cmd_result(cmd_str)
        if len(cmd_result) == 0 :
            return port
        else:
            return False

    def create_port_list(self,port):
        '''
        创建可用端口信息
        :return:
        '''
        port_list = []
        while len(port_list) != len(self.dev_list):
            new_port = self.check_port_used(port)
            if new_port :
                port_list.append(new_port)
            new_port += 1
        return port_list

    def create_appium_cmd_list(self,i):
        '''
        根据设备数创建server命令数
        命令：appium -p 4700 -bp 4900 -U devicesName --no-reset --session-override
        :return:
        '''
        start_p_port = 4700 + int(i)
        start_bp_port = 5000 + int(i)
        p_port_list = self.create_port_list(start_p_port)
        bp_port_list = self.create_port_list(start_bp_port)
        dev_list = self.dev_list
        appium_list = []
        cmd_str = "appium -p {0} -bp {1} -U {2} --no-reset --session-override".format(p_port_list[i],bp_port_list[i],dev_list[i])
        appium_list.append(cmd_str)
        self.wu.write_yaml(str(i),str(p_port_list[i]),str(bp_port_list[i]),str(dev_list[i]))
        return appium_list

    def exec_appium(self,i):
        '''
        单个启动appium服务
        :param i:
        :return:
        '''
        self.start_list = self.create_appium_cmd_list(i)
        self.doc.cmd_no_result(self.start_list[0])

    def kill_server(self):
        '''
        杀死appium得node进程
        :return:
        '''
        node_task = self.doc.cmd_result('tasklist | findstr node.exe')
        if node_task:
            self.doc.cmd_no_result("taskkill /f /pid node.exe")

    def start_appium_server_thread(self):
        '''
        多线程启动appium_server
        :return:
        '''
        self.kill_server()
        self.wu.clear_user_info()
        for i in range(len(self.find_devices())):
            appium_start = threading.Thread(target=self.exec_appium,args=(i,))      # 注意这里启动方式
            appium_start.start()
            time.sleep(13)


if __name__ == '__main__':
    s = AppServer()
    print(s.find_devices())
    s.start_appium_server_thread()