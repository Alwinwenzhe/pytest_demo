# -- coding:utf-8 --
import time, random, datetime

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

    def get_cur_date(self,*args,**kwargs):
        '''获取当前得日期'''
        return time.strftime("%Y-%m-%d")

    def get_cur_time_add(self,num=16, *args,**kwargs):
        '''
        获取当前时间并延后时间
        :param num:   默认延后10分钟
        :param args:
        :param kwargs:
        :return:
        '''
        return (datetime.datetime.now() + datetime.timedelta(minutes=num)).strftime("%H:%M")

    def get_time_int(self,cur_time='17:41'):
        '''时间延迟后，分钟数收为整数'''
        tim_list = cur_time.split(":")
        tim_list[1] = tim_list[1][0] + '0'
        return ":".join(tim_list)

    def morning_or_afternoon(self):
        '''判定时间是上午还是下午，这里有个问题，如果刚好卡在中午11.40左右，时间这里会出错'''
        cur_H = self.get_cur_time_add().split(":")[0]
        H = 'morning' if int(cur_H) <= 12 else 'afternoon'
        return H

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

if __name__ == '__main__':
    dt = DealTime()
    print(dt.get_cur_date())
    print(dt.morning_or_afternoon())
    print(dt.get_time_int())