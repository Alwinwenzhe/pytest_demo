import ast, xlrd
from openpyxl.styles import PatternFill, Font
from data import Config
from common import operate_json

class ExcelHandler(object):
    '''
    关于Excel表的操作
    '''
    oper_j = operate_json.OperateJson()
    con = Config.Config()

    def get_excel_data(self,case_desc,sheet_index=0):
        '''
        可以通过参数：file_name文件名来区分不同数据，对应不同的函数入口
         数据文件过滤excel中不必要的数据
        :param file_name: 通过他来区分是接口还是web 数据文件
        :param case_desc: 通过excel中的case_description来过滤用例
        :return:
        '''
        # 获取到book对象
        book = xlrd.open_workbook(Config.API_CASE_PATH)       # 注意：这里已经写死了是接口测试对应的文件路径，并没有参数化
        sheet = book.sheet_by_index(sheet_index)              # 这里就默认运行的第一个，也就是debug

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        title = sheet.row_values(0)
        # 获取其他行
        for i in range(1, rows):
            #print(sheet.row_values(i))
            if case_desc in sheet.row_values(i):
                l.append(dict(zip(title, sheet.row_values(i))))  # 先返回一个zip对象，按最短得title或row_values拼接；然后通过dict格式化为dict，最后增加到list中
        return l

    def write_excel(self,keys,sheet,values,name):
        '''
        写入数据到excel
        :param sheet: 当前sheet
        :param values: 读取得数据内容
        :param name: sheet得name
        :return:
        '''
        para = self.str_to_dict(values[2])
        result = getattr(keys, values[1])(**para)
        if result:
            print('Case：{}，执行成功'.format(name))
            # sheet.cell(values[0] + 1, column=5).value('Pass')
            self.write_result(sheet.cell,values[0]+1,5,'Pass')
        else:
            print('Case：{}，执行失败'.format(name))
            # sheet.cell(values[0] + 1, column=5).value('False')
            self.write_result(sheet.cell,values[0]+1,5,'Fail')

    def str_to_dict(self,str_data):
        '''
        将字符串格式得数据转化为python可识别得dict格式;比使用json.loads更好，因为str如果内容是单引号会报错
        :param str_data:
        :return:
        '''
        return ast.literal_eval(str_data)

    def write_result(self,cell,row,column,result):
        '''设置Pass样式'''
        if result == 'Pass':
            color = 'AACF91'        # 绿色
            # 写入内容
            cell(row,column).value = 'Pass'
        elif result == "Fail":
            color = 'FF0000'  # 红色
            # 写入内容
            cell(row, column).value = 'Fail'
        # 单元格样式定义：绿色+加粗
        cell(row, column).fill = PatternFill('solid', color)  # 设置颜色
        cell(row, column).font = Font(bold=True)  # 加粗

if __name__ == '__main__':
    eh = ExcelHandler()
    print(eh.get_excel_data(r'../../data/接口测试用例.xlsx'))

