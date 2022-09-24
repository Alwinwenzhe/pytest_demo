# -*- coding:utf-8 -*-
import os

class DosCmd(object):

    def cmd_result(self,command):
        '''
        执行cmd命令，并返回脚本执行的输出内容作为返回值
        :param command:
        :return:
        '''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def cmd_no_result(self,command):
        '''
        执行cmd命令，返回值是脚本的退出状态码，只会有0(成功),1,2
        :param command:
        :return:
        '''
        os.system(command)

if __name__ == '__main__':
    doc = DosCmd()
    # print(doc.cmd_result('adb devices'))
    # print('间隔'.center(20,"*"))
    t = doc.cmd_result('netstat -ano | findstr 4700')
    p = doc.cmd_result('pip list')
    print(t)