# -- coding:utf-8 --
import time, random
from datetime import datetime, timedelta
from common import operate_json
from common.yaml_util import YamlUtil


class DealTime(object):

    def __init__(self):
        self.ya = YamlUtil()
        self.oper_j = operate_json.OperateJson()

    def get_current_timestamp(self, jmb=False, *args, **kwargs):
        '''
        当前时间的时间戳获取,
        :return:
        '''
        if jmb:  # 姐妹邦的时间戳会增加一个随机数
            time_st = int(time.time())  # 强制将得到的浮点数进行转化
            time_stru = str(time_st) + "-" + str(self.randint())
        else:
            time_stru = int(time.time())  # 强制将得到的浮点数进行转化
        return time_stru

    def write_time_to_json(self):
        '''
        把时间戳写入json文件
        :return:
        '''

        self.oper_j.write_json_value(oa_start_stamp=self.get_current_timestamp(), cur_date=self.get_cur_date(),
                                     oa_end_stamp=self.get_current_timestamp() + 3600,
                                     reimburse_Date=self.get_current_timestamp(),
                                     cur_time_stf=self.get_current_timestamp(),
                                     cur_date_time=self.get_cur_date_time(),
                                     cur_date_time_delay_6hours=self.get_cur_date_time_delay_housr())

    def get_cur_date_time(self):
        # 获取当前时间
        current_time = datetime.now()
        # 格式化当前时间为指定格式
        return current_time.strftime("%Y-%m-%d %H:%M")

    def get_cur_date_time_delay_housr(self, delay_times=6):
        '''
        获取当前时间往后推6小时
        :param delay_hours:
        :return:
        '''
        # 获取当前时间
        current_time = datetime.now()
        # 将当前时间往后推6小时
        current_time_plus_6_hours = current_time + timedelta(hours=delay_times)
        # 格式化这个时间
        return current_time_plus_6_hours.strftime("%Y-%m-%d %H:%M")

    def get_cur_date(self, *args, **kwargs):
        '''获取当前得日期'''
        return time.strftime("%Y-%m-%d")

    def join_time(self, hm):
        '''
        将传入小时分钟，转化为时间戳
        :param hm:
        :return:
        '''
        pass

    def get_cur_time_add_and_write(self, num=16, *args, **kwargs):
        '''
        获取当前时间并延后时间,并将延后得时间转化为时间戳写入配置
        :param num:   默认延后10分钟
        :param args:
        :param kwargs:
        :return:
        '''
        delay_hole_time = datetime.datetime.now() + datetime.timedelta(minutes=16)
        # 分割处理时间
        s_time = (str(delay_hole_time).split('.')[0]).split(":")
        if int(s_time[1][1]) - 5 > 0:
            s_time[1] = s_time[1][0] + '5'
        else:
            s_time[1] = s_time[1][0] + '0'
        hole_time = ":".join(s_time)
        tt = datetime.datetime.strptime(hole_time, "%Y-%m-%d %H:%M:%S")
        un_time = int(time.mktime(tt.timetuple()))
        self.ya.write_inter_yaml('start_time_stamp', un_time)
        delay_h_m = tt.strftime("%H:%M")
        return delay_h_m

    def get_cur_time_add(self, num=16, *args, **kwargs):
        '''
        获取当前时间并延后时间,并将延后得时间转化为时间戳写入配置
        :param num:   默认延后10分钟
        :param args:
        :param kwargs:
        :return:
        '''
        delay_hole_time = datetime.datetime.now() + datetime.timedelta(minutes=num)
        delay_h_m = self.get_time_int(delay_hole_time.strftime("%H:%M"))
        return delay_h_m

    def get_time_int(self, cur_time='17:41'):
        '''时间延迟后，分钟数收为整数'''
        s_time = cur_time.split(":")
        if int(s_time[1][1]) - 5 > 0:
            s_time[1] = s_time[1][0] + '5'
        else:
            s_time[1] = s_time[1][0] + '0'
        return ":".join(s_time)

    def morning_or_afternoon(self, start_time):
        '''判定时间是上午还是下午，这里有个问题，如果刚好卡在中午11.40左右，时间这里会出错'''
        cur_H = start_time.split(":")[0]
        H = 'morning' if int(cur_H) <= 12 else 'afternoon'
        return H

    def get_str_time(self, *args, **kwargs):
        '''
        获取当前格式化时间
        :return:
        '''
        return time.strftime("%Y-%m-%d %H:%M", time.localtime())

    def randint(self, len=3, *args, **kwargs):
        '''
        指定几位随机数
        :return:
        '''
        rand_len = 10 ** len - 1  # 次方
        rand_int = random.randint(0, rand_len)
        return rand_int

    def wait_until_start(self, start_time, wait_time=8):
        '''
        判定开始后才进入抽签环节
        :param start_time: 传入时间戳格式
        :param wait_time:
        :return:
        '''
        # 仅显示当前时分
        wait_s = wait_time * 60
        while True:
            cur_time = int(time.time())
            else_time = int(start_time) - cur_time
            if else_time < wait_s:
                print('距离抽签时间小于{0}分钟，可开始抽签'.format(wait_time))
                break
            else:
                print("抽签时间未到，请等待30s")
                time.sleep(30)


if __name__ == '__main__':
    dt = DealTime()
    dt.write_time_to_json()
