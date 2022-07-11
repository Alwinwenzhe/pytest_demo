# -- coding:utf-8 --
import os

class Oper_File(object):

    def del_file(self,path):
        ls = os.listdir(path)       # 收集指定路径下的文件及目录
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.del_file(c_path)   # 递归
            else:
                os.remove(c_path)

