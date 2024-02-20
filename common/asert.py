# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午10:14
# @Author  : WangJuan
# @File    : asert.py


"""
封装Assert方法

"""
from common import my_log
from common import consts
import json,requests, pytest


class Asert(object):

    def __init__(self):
        self.log = my_log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except Exception as e:
            print("\033[32;1m出现错误如下\033[0m")
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except Exception as e:
            print("\033[32;1m出现错误如下\033[0m")
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证接口response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)         # 将body序列化为JSON格式的str
            assert expected_msg in text
            return True
        except Exception as e:
            print("\033[32;1m出现错误如下\033[0m")
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证接口response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True
        except Exception as e:
            print("\033[32;1m出现错误如下\033[0m")
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            consts.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True
        except Exception as e:
            print("\033[32;1m出现错误如下\033[0m")
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            consts.RESULT_LIST.append('fail')
            raise


    def assert_easy(self,res_code,res_time):
        '''
        仅判断响应状态及响应时间:适用于php
        :return:
        '''
        assert self.assert_code(res_code, 200)
        assert self.assert_time(res_time, 1500)

    #     以下方法使用装饰器没弄好
    # def assert_easy(self,*args,**kwargs):
    #     '''
    #     仅判断响应状态及响应时间:适用于php
    #     :return:
    #     '''
    #     assert self.assert_code(args[0], 200)
    #     assert self.assert_time(args[1], 1500)
    #     def sert_easy(func):
    #         def easy(*args,**kwargs):
    #             func(*args,**kwargs)
    #             return easy
    #         return sert_easy
    #
    # @assert_easy(res_code,res_time)

    def assert_common(self,res_code,res_body,res_expect,res_time):
        '''
        通用常用三个维度验证
        :param res_code: 接口响应代码
        :param res_body: 接口响应内容
        :param res_expect: 接口响应期望值
        :param res_time: 接口响应时间
        :return:
        '''
        assert self.assert_code(res_code, 200)
        assert self.assert_in_text(res_body, res_expect)
        assert self.assert_time(res_time, 1500)

    def assert_yaml(self,assert_info,res,mylog):
        '''验证yaml中的包含与相等'''
        if 'contains' in assert_info.keys():
            # assert assert_info['contains'] in res
            pytest.assume(assert_info['contains'] in res,f'期望验证信息是：{assert_info},实际信息是：{res}')
        elif 'equals' in assert_info.keys():
            # assert assert_info['equals'] == res
            pytest.assume(assert_info['equals'] == res,f'期望验证信息是：{assert_info},实际信息是：{res}')
        # 这里需要判断ture false 对应不同得日志级别，不仅是info
        mylog.info('用例执行完毕')



