# import sys
# sys.path.append(r"D:\Job\python\Script\Api_automation")
from common import operate_json
from data import Config
import pymysql
import re


class OperateSqlAl(object):
    oj = operate_json.OperateJson()
    con = Config.Config()

    def __init__(self, envir):
        if 'ysy_test' == envir:  # 一生约测试
            self.dbhost = self.con.tysy_db_host
            self.dbport = int(self.con.tysy_db_port)
            self.dbname = self.con.tysy_db_name
            self.db_user = self.con.tysy_db_user
            self.pwd = self.con.tysy_db_pwd
        elif 'and_oa' == envir:
            self.dbhost = self.con.oa_db_host
            self.dbport = int(self.con.oa_db_port)
            self.dbname = self.con.oa_db_name
            self.db_user = self.con.oa_db_user
            self.pwd = self.con.oa_db_pwd

    def re_sql(self, var_str):
        """
        处理str中包含了变量的sql
        :param str:可能包含了formate的字符串
        :return:不包含了formate的字符串
        """
        if 'format' in var_str:
            p1 = re.compile(r"[(](.*?)[')]", re.S)
            split_str = var_str.split('format')
            var_1 = re.findall(p1, split_str[1])
            # 这里会对list中每个值进行判断
            var_1 = self.dd.circular_processing_data(var_1)
            # 注意这里只传递了第一个格式化值进来
            sql_resutl = split_str[0].format(*var_1)
            return sql_resutl
        else:
            return var_str

    def execute_sql(self, sql_str):
        try:
            db = pymysql.connect(host=self.dbhost, port=self.dbport, user=self.db_user, passwd=self.pwd, db=self.dbname,
                                 charset='utf8')
            cursor = db.cursor()  # 创建一个游标
            cursor.execute(sql_str)
            data = cursor.fetchone()
            data = self.bytes_to_str(data[0])
            return data
        except Exception:
            print('\033[1;33m"sql执行异常，请检查"\033[0m \n')
        finally:
            cursor.close()
            db.close()  # 关闭数据库

    def bytes_to_str(self, val1):
        if type(val1) == bytes:
            val1 = val1.decode(encoding='utf-8')
        return val1

    def sql_main(self, data):
        '''
        这里的多个sql语句执行后，结果可能是一个变量或一个list并未做处理
        :param data:
        :return:
        '''
        if ';' in data:
            split_data = data.split(";")
            for i in split_data:
                value = self.execute_sql(i)  # 相互调用异常
                return value
        else:
            return self.execute_sql(data)


if __name__ == "__main__":
    om = OperateSqlAl("and_oa")
    resl = om.sql_main(
        "SELECT su.username from system_users su WHERE su.nickname = '苟海军'")
    print(type(resl), resl)  # 返回结果默认为tuple
    # print(oy.read_yaml()['db']['release']['user'])
