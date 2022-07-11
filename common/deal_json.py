# -- coding:utf-8 --
from common.data_md5 import DataMd5

class DealJson(DataMd5):       # 没必要使用多继承
    '''json处理'''

    def write_data_to_json(self, *args,**kwargs):
        '''
        将当前时间戳写入json
        将随机8位数戳写入json
        将登录标记写入json
        :return:
        '''
        rand8,cur_ti,sign = self.ysy_sign_md5()   # 不能单独调用，否则时间戳等会不同
        self.oper_j.write_json_value(curTime = cur_ti,nonce=rand8,sign=sign)

    # def write_jmb_sign_to_json(self,func):
    #     '''
    #     姐妹邦对应的sign等信息写入json
    #     :return:
    #     '''
    #     def inner_write_jmb_sign_to_json(self,*args,**kwargs):
    #         sign, cur_ti, rand3 = self.jmb_sign_md5()  # 不能单独调用，否则时间戳等会不同
    #         mobile_sign = self.jmg_mobile_sign()
    #         self.oper_j.write_json_value('curTime', cur_ti)
    #         self.oper_j.write_json_value('nonce', rand3)
    #         self.oper_j.write_json_value('sign', sign)
    #         self.oper_j.write_json_value('mobile_sign',mobile_sign)
    #         func(args,kwargs)
    #     return inner_write_jmb_sign_to_json
    def write_jmb_sign_to_json(self):
        '''
        姐妹邦对应的sign等信息写入json
        :return:
        '''
        sign, cur_ti, rand3 = self.jmb_sign_md5()  # 不能单独调用，否则时间戳等会不同
        mobile_sign = self.jmg_mobile_sign()
        self.oper_j.write_json_value(curTime = cur_ti,nonce=rand3,sign=sign,mobile_sign=mobile_sign)
