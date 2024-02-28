import ast
import os

import openpyxl
from common.web_common.web_key import WebKey
from common.excel_handler import ExcelHandler


def get_test_file():
    # 获取指定路径下的所有测试用例文件
    for path, dir, files in os.walk(r'../../data'):  # 目录树生成器
        # print('打印当前路径：',path)
        # print("当前路径文件夹：",dir)
        # print('当前路径文件：',files)
        for i in files:  # 获取根路径下的所有文件
            if i.endswith('xlsx'):
                data_file = path + '/' + i  # 拼接文件完整路径
                print('即将开始测试文件：{}'.format(data_file).center(40, '>'))
            elif i.endswith('dis'):
                print('该文件用例已被弃用，可以写入日志'.center(40, '>'))

def read_excel(file):
    '''获取excel内存对象'''
    excel = openpyxl.load_workbook(file)
    return excel


def init_driver(case_para):
    '''初始化浏览器'''
    try:
        if case_para[1] == 'open_browser':  # 实例化，通过一个操作行为实例化官架子驱动类对象
            browser_type = ast.literal_eval(case_para[2])
            keys = WebKey(**browser_type)
            return keys
    except Exception as e:
        print(e)

def exec_case(case_para, keys, sheet, name, excel, file):
    '''执行case中的各种操作，网上可以封装传递变量参数，这里就是用例执行'''
    if 'assert' in case_para[1]:  # 断言用例执行是否成功
        ExcelHandler().write_excel(keys, sheet, case_para, name)
        excel.save(file)
    else:
        para = ExcelHandler().str_to_dict(case_para[2])
        getattr(keys, case_para[1])(**para)  # 传入参数不能是list，必须解析
        # 这里得参数个数不同，之前只通过dict取值，现在需要对数据进行处理



def del_dict_None(para):
    '''
    将para中None值删除掉
    :param para: 传入得时tuple
    :return:
    '''
    t2 = []
    for i in para:
        if i != None:
            t2.append(i)
    return t2

if __name__ == '__main__':
    # get_test_file(r'../../data/web_test_qiuyi.xlsx')
    print(read_excel(r'../../data/web_test_baidu.xlsx').sheetnames)