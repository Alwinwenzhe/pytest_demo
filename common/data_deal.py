import json, re, time, hashlib, random, datetime, os, jsonpath
from common import my_log
from common import operate_json
from data import Config
from common import operate_sql_al
from common import excel_handler
from common import req_reload
from common import asert
from common import consts
from common.deal_time import DealTime


class DataDeal(object):
    '''基础的处理'''

    def __init__(self):
        self.log = my_log.MyLog()
        self.oper_j = operate_json.OperateJson()
        self.conf = Config.Config()
        self.excel = excel_handler.ExcelHandler()
        self.reqe = req_reload.ReqReload()
        self.test = asert.Asert()
        self.dl = DealTime()

    def choose_envir(self, envir):
        '''
        运行环境判断-反射
        从config.py文件中找到对应属性
        :param envir:
        :return: 请求url域名
        '''
        try:
            temp = getattr(self.conf, envir)  # 获取成员并返回
            return temp
        except Exception as e:
            print('环境变量设置有误：{}'.format(e))

    def param_get_deal(self, case, request_mode='get'):
        '''
        case参数获取并进行相关处理
        :param case:
        :return:
        '''
        request_mode = case['request_mode']
        envir = case['envir']
        expect = case['case_expect']
        preset_data = case['case_preset']
        urls = case['case_url']
        global_var = case['case_global_var']
        upload_files = case['upload_files']
        url_domain = self.choose_envir(envir)
        api_url = url_domain + urls
        api_url = self.while_data(envir, api_url)  # url不会有多个且复杂的处理，所有可以直接使用while_data
        if expect:
            expect = self.while_data(envir, expect)
        if preset_data:
            self.single_sql_data_deal(envir, preset_data)  # 返回值都写进json了
        if case['case_header']:  # 判断header是否为空
            headers = json.loads(case['case_header'])  # 把字符串转换成python能识别的dict数据类型
            headers = self.brackets_dict_data(envir, headers)
        else:
            headers = None
        params = case['case_params']
        if params:
            params = json.loads(params)  # 将字符串通过特殊的形式转为python的dict类型
            params = self.brackets_dict_data(envir, params)  # params格式有问题
        return request_mode, expect, api_url, headers, params, global_var, upload_files  # 只验证第一个expect值即可

    def single_sql_data_deal(self, envir, data, *args, **kwargs):
        '''
        首先判断'$$'，其次判断'formate',最后判断干净sql
        :param data:
        :param envir:
        :return:
        '''
        oper_s = operate_sql_al.OperateSqlAl(envir)
        if '$$' in data and 'format' in data:
            # 将$$识别为即将执行sql并写入json
            symbol_data = data.split('$$')
            sql_str = self.format_data(envir, symbol_data[1])
            val = oper_s.execute_sql(sql_str)
            self.oper_j.write_json_value(symbol_data[0], val)
            # return None
        elif "$$" in data and 'format' not in data:
            symbol_data = data.split('$$')
            sql_str = self.while_data(envir, symbol_data[1])
            val = oper_s.execute_sql(sql_str)
            self.oper_j.write_json_value(symbol_data[0], val)
            # return None
        elif 'format' in data:
            val = self.format_data(envir, data)
            val = oper_s.execute_sql(val)
            return val
        else:
            val = oper_s.execute_sql(data)
            return val

    def brackets_dict_data(self, envir, data, *args, **kwargs):
        '''
        处理通过dict来输入的多个数据，包括嵌套的字典和列表。
        :param envir: 环境变量或其他上下文信息
        :param data: 待处理的字典数据
        :return: 处理后的字典数据
        '''
        for key, value in data.items():
            if isinstance(value, dict) and "::" in str(value):
                # 处理字典
                for k, v in value.items():
                    if isinstance(v, (dict, list)) and "::" in str(v):
                        # 如果值是字典或列表，递归处理
                        data[key][k] = self.brackets_dict_data(envir, v)
                    elif "::" in str(v):
                        # 如果值是普通类型，调用处理函数
                        data[key][k] = self.circular_processing_data(envir, v)
            elif isinstance(value, list) and "::" in str(value):
                # 处理列表
                for i, item in enumerate(value):
                    if isinstance(item, (dict, list)):
                        # 如果列表中的元素是字典或列表，递归处理
                        data[key][i] = self.brackets_dict_data(envir, item)
                    else:
                        # 如果列表中的元素是普通类型，调用处理函数
                        data[key][i] = self.circular_processing_data(envir, item)
            elif "::" in str(value):
                # 非字典和非列表的值进行处理
                data[key] = self.circular_processing_data(envir, value)
            else:
                pass
        return data

        # def brackets_dict_data(self, envir, data, *args, **kwargs):

    #     '''
    #      处理通过dict来输入的多个数据，比如dict， 针对dict中多个内容
    #     :param data:
    #     :param envir:
    #     :return:
    #     '''
    #     for key, value in data.items():
    #         if isinstance(value, dict):
    #             new_value = value
    #             for k, v in new_value.items():
    #                 new_value[k] = self.circular_processing_data(envir, v)
    #             data[key] = new_value
    #         else:
    #             data[key] = self.circular_processing_data(envir, value)
    #     return data

    def format_data(self, envir, data, *args, **kwargs):
        '''
        处理数据中包含formate的待处理数据
        :param data:
        :return:
        '''
        p1 = re.compile(r"[(](.*?)[)]", re.S)  # 非贪心匹配
        split_str = data.split('format')
        var_1 = re.findall(p1, split_str[1])  # 利用正则：去掉括号，找出所有匹配结果
        # 这里会对list中每个值进行判断
        # var_1 = self.while_split_data(envir, var_1)  #这里怎么会传入list？
        list_var = var_1[0].split(',')
        result_forma_data = []
        for i in list_var:
            result_forma_data.append(self.while_data(envir, i))
        resutl = split_str[0].format(
            result_forma_data)  # 这format函数会自动将参数转换成一个元组，所以如果你本来想传入一个元组参数到format函数中的话，实际上参数为长度为1的元组中嵌套你传的元组。
        # 所以前面的{0}，{1}，{2}…要改成 {0[0]} {0[1]}…
        return resutl

    def circular_processing_data(self, envir, data, *args, **kwargs):
        '''
        处理空list，str
        :param envir:
        :param data:
        :return:
        '''
        if isinstance(data, str):  # 判断是否是str类型
            data = self.split_data(envir, data)
        elif isinstance(data, list):  # 判断是否是list类型
            new_data = []
            for i in data:
                i = self.split_data(envir, i)
                new_data.append(i)
                data = new_data[0]  # 如果是list返回第一个值即可
        return data

    def split_data(self, envir, data, *args, **kwargs):
        '''

        区分str中是否带有’&‘标识：有：首先split变量,
        :param data:
        :return:
        '''
        if '&' in data:
            data = data.split("&")
            result = []
            for i in data:
                i = self.while_data(envir, i)
                result.append(i)
            temp = '&'
            data = temp.join(result)
        else:
            data = self.while_data(envir, data)
        return data

    def while_data(self, envir, data, *args, **kwargs):
        '''
        持续判断data中是否包含以下几种类型变量，如果有，则对每种情况处理一次
        :param data:
        :return:
        '''
        # oper_s = operate_sql_al.OperateSqlAl(envir)
        while 'j::' in data or 'c::' in data or 's::' in data or '@time@' in data:
            if 'j::' in data:
                symbol_data = data.split('j::')  # 这里有可能是body中的某个值传入，如：'j::verifyCode'
                con_data = str(self.oper_j.get_json_value(symbol_data[1]))
                data = symbol_data[0] + con_data  # 拼接前需做type统一
                # data = self.is_num_by_except(data)         # 纯数字判断，不能加，加了登录接口的验证码和手机号被当作纯数字，出问题
                return data
            elif 'c::' in data:
                symbol_data = data.split('c::')
                con_data = self.choose_envir(symbol_data[1])
                data = symbol_data[0] + con_data
                return data
            elif '@time@' in data:  # 处理需要特殊处理的变量，如时间变量
                symbol_data = data.split('@time@')
                data = symbol_data[0] + self.dl.get_str_time() + symbol_data[1]
                return data
            elif 's::' in data:
                oper_s = operate_sql_al.OperateSqlAl(envir)
                symbol_data = data.split('s::')
                con_data = oper_s.sql_main(symbol_data[1])  # 這裡不能調用con_var方法
                data = con_data
                return data
            else:
                return data
                break
        else:
            return data

    def response_write_to_json(self, key, res, *args, **kwargs):
        '''
        通过key在res中不断寻找对应value
        :param path:
        :param response:
        :return:
        '''
        list_comma = key.split(',')
        for i in list_comma:
            list = i.split("/")
            res_value = json.loads(res)  # 序列化字符串或json对象成为python对象
            try:
                for i in list[1::]:
                    if i.isdigit():  # 如果是数字
                        res_value = res_value[int(i)]
                    elif ":" in i:
                        list2 = i.split(":")
                        if list2[0] in res_value:
                            res_value = res_value[list2[0]]
                    elif i in res_value:
                        res_value = res_value[i]
                if ":" in list[-1]:
                    self.oper_j.write_json_value(list2[1], res_value)
                else:
                    self.oper_j.write_json_value(list[-1], res_value)
            except Exception as e:
                self.log.error('error log：get param fail')

    def filter(self, value, res_value):
        '''过滤数据'''
        if value.isdigit():  # 如果是数字
            res_value = res_value[int(value)]
        elif ":" in value:
            list = value.split(":")
            if list[0] in res_value:
                res_value = res_value[list[0]]
        elif value in res_value:
            res_value = res_value[value]
        return list, res_value

    def test_case_method(self, case, *args, **kwargs):
        '''
        所有api测试用例调用该方法
        :param case:
        :param request_method:
        :return:
        '''
        request_method, expect, api_url, headers, params, global_var, upload_files = self.param_get_deal(case)
        response = self.reqe.req(request_method, api_url, params, headers, upload_files)
        if response['body']:
            self.test.assert_common(response['code'], response['body'], expect, response['time_consuming'])
        else:  # 处理PHP返回的页面请求
            self.test.assert_easy(response['code'], response['time_consuming'])
        consts.RESULT_LIST.append('True')
        if global_var:
            self.response_write_to_json(global_var, response['text'])
        print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'], case['case_description'], expect))
        time.sleep(2)

    def randint(self, len=3, *args, **kwargs):
        '''
        指定几位随机数
        :return:
        '''
        rand_len = 10 ** len - 1  # 次方
        rand_int = random.randint(0, rand_len)
        return rand_int

    # 获取指定文本信息
    def get_text(self, res, key):
        if res is not None:
            try:
                txt = json.loads(res)
                value = jsonpath.jsonpath(txt, "$..{0}".format(key))  # 可以从txt中寻找需要的key值
                # jsonpath获取成功就返回list，获取失败就返回False
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None

    def deal_yaml_data(self):
        '''处理yaml中得变量数据'''
        yaml_data = '${get_base_url(ysy_base_url)}'

    def get_current_timestamp(self):
        return self.dl.get_current_timestamp()


if __name__ == '__main__':
    ut = DataDeal()
    # print(self.dt.get_current_timestamp(jmb=1))
    # print(self.dl.get_cu)
    # print(ut.jmb_sign_md5())
    # print(ut.jmg_mobile_sign())
    # print(ut.randint_8())
    print(ut.get_current_timestamp())
    # print(ut.while_split_data('test_debug',"s::SELECT IFNULL(dv.version,'error_version') FROM data_version dv WHERE dv.code='ios'"))
