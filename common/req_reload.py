# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:22
# @Author  : WangJuan
# @File    : Request.py

"""
封装request

"""

import os, json
import random
import requests
from requests_toolbelt import MultipartEncoder
from common import consts


class ReqReload(object):

    # def __init__(self, env):  和下方的self.get_session = self.session.get_session(env)配套使用
    # def __init__(self):
    #     """
    #     :param env:
    #     """
    #     self.session = Session.Session()
    #     # self.get_session = self.session.get_session(env)
    #     self.get_session = self.session.get_session('debug')

    def req(self,api_method,api_url, params, headers):
        '''
        封装请求方法
        :param api_method:
        :param api_url:
        :param params:
        :param headers:
        :return:
        '''
        # s = requests.sessions
        # s.keep_alive = False  # 关闭多余连接
        if 'get' == api_method:
            res = self.get_request(api_url, params, headers)
        elif 'post' == api_method:
            res = self.post_request(api_url, params, headers)
        elif 'put' == api_method:
            res = self.get_request(api_url, params,headers)
        return res

    def get_request(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        # 无需判定url开头
        # if not url.startswith('http://'):
        #     url = '%s%s' % ('http://', url)
        #     print(url)

        # 这里登录暂时未使用cookies，所有源代码暂时注释掉
        # try:
        #     if data is None:
        #         response = requests.get(url=url, headers=header, cookies=self.get_session)
        #     else:
        #         response = requests.get(url=url, params=data, headers=header, cookies=self.get_session)
        try:
            response = requests.get(url, params=data, headers=header,verify=False)
        except requests.RequestException as e:
            print(' \033[31m RequestException url: %s \033[0m ', url)
            print(e)
            return ()
        # 這裏需要兩個異常嗎？
        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        return response_dicts

    def post_request(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        # # 配置裡就寫死了，不需要
        # if not url.startswith('https://'):
        #     url = '%s%s' % ('https://', url)
        #     print(url)

        try:
            response = requests.post(url=url, data=json.dumps(data), headers=header,verify=False)
                # response = requests.post(url=url, data=data, headers=header)
        # try:
        #     if data is '':
        #         response = requests.post(url=url, headers=header, cookies=self.get_session)
        #     else:
        #         response = requests.post(url=url, params=data, headers=header, cookies=self.get_session)
        except requests.RequestException as e:
            print(' \033[31m RequestException url: %s \033[0m', url)  #设置了字符串显示样式和显示后的样式
            print(e)
            return None
        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()
        consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session,verify=False)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print(' \033[31m RequestException url: %s \033[0m ', url)
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=self.get_session,verify=False)
            else:
                response = requests.put(url=url, params=data, headers=header, cookies=self.get_session,verify=False)

        except requests.RequestException as e:
            print(' \033[31m RequestException url: %s \033[0m ', url)
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
