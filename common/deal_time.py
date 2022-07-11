# -- coding:utf-8 --
import time, random

class DealTime(object):

    def get_current_timestamp(self, jmb=False, *args, **kwargs):
        '''
        当前时间的时间戳获取,
        :return:
        '''
        if jmb:  # 姐妹邦的时间戳会增加一个随机数
            time_st = int(time.time() * 1000)  # 强制将得到的浮点数进行转化
            time_stru = str(time_st) + "-" + str(self.randint())
        else:
            time_stru = int(time.time() * 1000)  # 强制将得到的浮点数进行转化
        return time_stru

    def get_str_time(self, *args,**kwargs):
        '''
        获取当前格式化时间
        :return:
        '''
        return time.strftime("%Y-%m-%d %H:%M", time.localtime())

    def randint(self,len=3, *args,**kwargs):
        '''
        指定几位随机数
        :return:
        '''
        rand_len = 10 ** len - 1        # 次方
        rand_int = random.randint(0,rand_len)
        return rand_int