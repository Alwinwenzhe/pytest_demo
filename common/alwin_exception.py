# -*- coding: utf-8 -*-

class AlwinException(Exception):
    '''自定义异常待填充'''
    def __init__(self,msg=None):
        self.msg = msg

    def __str__(self):          # 定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
        if self.msg:
            return self.msg
        else:
            return "other error!"

if __name__ == "__main__":
    try:
        raise AlwinException('test error!')  # 主动出发自定义异常
    except Exception as e:
        print(e)
