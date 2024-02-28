# -- coding:utf-8 --
from common.deal_time import DealTime
from common.data_deal import DataDeal
import hashlib, datetime

class DataMd5(DataDeal,DealTime):  # 新式类：多继承广度优先
    '''处理需要加密的数据'''

    def ysy_sign_md5(self, *args,**kwargs):
            '''
            一生约正式环境登录接口的签名规则
            :return:
            '''
            key = 'MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALe39vUUq6T1NBMg4QoEyl96WKYdHrGUvYIMRDIIaHZbu1eLeYEiesV/XNMwLyzXVZwmy9WpyNBTdDpQ'
            rand8 = self.randint(8)
            cur_ti = self.get_current_timestamp()
            str_sum = str(rand8) + key + str(cur_ti)
            str_re = str_sum.encode(encoding='utf-8')
            m = hashlib.md5()
            m.update(str_re)  #  md5,第一次加密
            n = hashlib.md5()  # 再次定义一个hash对象，因为重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖
            str_rb = m.hexdigest().encode(encoding='utf-8')
            n.update(str_rb)
            k = n.hexdigest()
            return rand8,cur_ti,k

    def jmb_sign_md5(self, *args,**kwargs):
        '''
        姐妹邦接口的签名规则
        :return:
        '''
        rand3 = self.randint()
        cur_ti = self.get_current_timestamp(jmb=True)
        str_sum = str(rand3) + str(cur_ti) + "jmbon88888888@"
        str_re = str_sum.encode(encoding='utf-8')
        m = hashlib.md5()                                   # 声明md5方法
        m.update(str_re)                                    #  md5加密
        sign = m.hexdigest().encode(encoding='utf-8')     # 以十六进制数字字符串的形式返回摘要值。
        sign = str(sign,encoding='utf-8')                 # 将上一行得到的byte类型数据转化为str
        return sign,cur_ti,rand3

    def jmg_mobile_sign(self, mobile='15828022852', *args,**kwargs):
        '''
        姐妹邦mobile_sign加密
        :return:
        '''
        cur_year = datetime.datetime.now().year         # 获取当前年份
        str_join = str(cur_year) + mobile + "jmbon"
        str_en = str_join.encode(encoding='utf-8')
        m = hashlib.md5()
        m.update(str_en)
        mobile_sign = m.hexdigest().encode(encoding='utf-8')
        sign = str(mobile_sign, encoding='utf-8')
        return sign

if __name__ == "__main__":
    dm = DataMd5()
    print(dm.jmg_mobile_sign())