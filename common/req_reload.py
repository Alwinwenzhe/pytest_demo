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
    requests.packages.urllib3.disable_warnings()

    # def __init__(self, env):  和下方的self.get_session = self.session.get_session(env)配套使用
    # def __init__(self):
    #     """
    #     :param env:
    #     """
    #     self.session = Session.Session()
    #     # self.get_session = self.session.get_session(env)
    #     self.get_session = self.session.get_session('debug')

    def req(self, api_method, api_url, params, headers, upload_files):
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
        if 'get' == api_method.lower():
            res = self.get_request(api_url, params, headers)
        elif 'post' == api_method.lower():
            res = self.post_request(api_url, params, headers, upload_files)
        elif 'put' == api_method.lower():
            res = self.put_request(api_url, params, headers)
        elif 'delete' == api_method.lower():
            res = self.delete_request(api_url, headers)
        else:
            res = self.post_request()
        return res

    def get_request(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        try:
            response = requests.get(url, params=data, headers=header, verify=False)
        except requests.RequestException as e:
            print(e)
            return ()
        # 這裏需要兩個異常嗎？
        except Exception as e:
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
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

    def post_request(self, url, data, header, upload_files):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        try:
            if upload_files:
                response = requests.post(url=url, files=eval(upload_files), headers=header, verify=False)
            else:
                response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
        except requests.RequestException as e:
            print(e)
            return None
        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
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
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session, verify=False)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type
                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )
                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header, cookies=self.get_session)
        except requests.RequestException as e:
            print(e)
            return ()
        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
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
        try:
            if data is None:
                response = requests.put(url=url, headers=header, verify=False)
            else:
                response = requests.put(url=url, json=data, headers=header, verify=False)
        except Exception as e:
            print(e)
            return ()
        time_consuming = response.elapsed.microseconds / 1000
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

    def delete_request(self, url, header):
        """
        Delete请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        try:
            response = requests.delete(url=url, headers=header, verify=False)
        except Exception as e:
            print(e)
            return ()
        time_consuming = response.elapsed.microseconds / 1000
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
