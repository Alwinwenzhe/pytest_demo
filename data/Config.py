# -*- coding: utf-8 -*-

from configparser import ConfigParser
from common import my_log
import os, re
# 工程中配置中有相对路径即可替代
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 脚本路径
# API_CASE_PATH = BASE_PATH + r'\data\base_student.xlsx'
API_CASE_PATH = BASE_PATH + r'\data\jnt_inter_case.xls'
QIUYI_CASE_PATH = BASE_PATH + r'\data\web_test_qiuyi.xlsx'
HC_CASE_PATH = BASE_PATH + r'\data\华测用例.xlsx'

class Config:
    # titles:
    TITLE_DEBUG = "private_debug"       # 定义类变量
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"

    # values:
    # [debug]
    # 一生约测试环境信息
    YSY_USER = "tester"
    YSY_ENVIRONMENT = "environment"
    YSY_HOST = "ysy_host"
    # 一生约测试环境数据库信息
    YSY_DB_HOST = "ysy_sql_dbhost"
    YSY_DB_PORT = "ysy_sql_dbport"
    YSY_DB_NAME = "ysy_sql_dbname"
    YSY_DB_USER = "ysy_sql_user"
    YSY_DB_PWD = "ysy_sql_pwd"
    # 雨花斋测试环境信息
    YHZ_HOST = "yhz_host"
    YHZ_DB_NAME = "yhz_db_name"
    YHZ_DB_USER = "yhz_db_user"
    YHZ_DB_PWD = "yhz_db_pwd"
    YHZ_TEST_USER = 'tyhz_user'
    # 姐妹邦测试环境
    JMB_T_HOST = "jmb_t_host"
    JMB_T_USER = "jmb_t_user"
    # 商城测试环境
    O2O_HOST = "ysyo2o_host"
    O2O_DB_NAME = 'ysyo2o_db_name'
    # 姐妹邦测试环境
    JMB_T_DB_HOST = "jmb_t_db_host"
    JMB_T_DB_NAME = "jmb_t_db_name"
    JMB_T_DB_USER = "jmb_t_db_user"
    JMB_T_DB_PWD = "jmb_t_db_pwd"
    JMB_T_DB_PORT = 'jmb_t_db_port'

    # [release] 下列数据中对应的值是没有的
    # 一生约正式环境信息
    YSY_USER = "ysy_user"
    YSY_HOST = 'ysy_host'
    YSY_USERID = "releaser_userId"
    YSY_ACCESSTOKEN = "releaser_accessToken"
    YSY_ENVIRONMENT = "environment"
    # 一生约正式环境数据库信息
    YSY_DB_HOST = "ysy_sql_dbhost"
    YSY_DB_PORT = "ysy_sql_dbport"
    YSY_DB_NAME = "ysy_sql_dbname"
    YSY_DB_USER = "ysy_sql_user"
    YSY_DB_PWD = "ysy_sql_pwd"
    # 一生约物业正式环境信息
    YSY_PRO_USER = "ysy_pro_user"
    YSY_PRO_HOST = "ysy_pro_host"
    # 商城正式环境
    O2O_HOST = "ysyo2o_host"
    O2O_DB_NAME = 'ysyo2o_db_name'
    # 雨花斋正式环境
    YHZ_USER = 'yhz_user'

    # 建能通APP測試環境
    JNT_APP_TEST = 'jnt_app_host'

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = my_log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        # print(self.conf_path)
        self.xml_report_path = Config.path_dir+'/allure-results'
        self.html_report_path = Config.path_dir+'/allure-report'
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')
        # 一生约测试环境信息
        self.tysy_host = self.get_conf(Config.YSY_HOST)
        self.tysy_user = self.get_conf(Config.YSY_USER)
        self.tysy_environment = self.get_conf(Config.YSY_ENVIRONMENT)
        self.ysy_test = self.get_conf(Config.YSY_HOST)
        # 一生约正式环境信息
        self.ysy_user = self.get_conf(Config.YSY_USER,'R')
        self.ysy_host = self.get_conf(Config.YSY_HOST,'R')
        self.ysy_userId = self.get_conf(Config.YSY_USERID,'R')
        self.ysy_accesstoken = self.get_conf(Config.YSY_ACCESSTOKEN,'R')
        self.ysy_environment = self.get_conf(Config.YSY_ENVIRONMENT,'R')
        self.ysy_release = self.get_conf(Config.YSY_HOST,'R')
        # 一生约测试环境数据库
        self.tysy_db_host = self.get_conf(Config.YSY_DB_HOST)
        self.tysy_db_port = self.get_conf(Config.YSY_DB_PORT)
        self.tysy_db_name = self.get_conf(Config.YSY_DB_NAME)
        self.tysy_db_user = self.get_conf(Config.YSY_DB_USER)
        self.tysy_db_pwd = self.get_conf(Config.YSY_DB_PWD)
        # 一生约正式环境数据库
        self.ysy_db_host = self.get_conf(Config.YSY_DB_HOST,'R')
        self.ysy_db_port = self.get_conf(Config.YSY_DB_PORT,'R')
        self.ysy_db_name = self.get_conf(Config.YSY_DB_NAME,'R')
        self.ysy_db_user = self.get_conf(Config.YSY_DB_USER,'R')
        self.ysy_db_pwd = self.get_conf(Config.YSY_DB_PWD,'R')
        # 雨花斋测试库信息，user和pwd和一生约测试一致
        self.tyhz_user = self.get_conf( Config.YHZ_TEST_USER)
        self.tyhz_db_user = self.get_conf(Config.YHZ_DB_USER)
        self.tyhz_db_pwd = self.get_conf(Config.YHZ_DB_PWD)
        self.yhz_test = self.get_conf( Config.YHZ_HOST)
        self.tyhz_db_name = self.get_conf(Config.YHZ_DB_NAME)
        # 雨花斋正式库信息
        self.yhz_user = self.get_conf(Config.YHZ_USER,'R')
        self.yhz_release = self.get_conf(Config.YHZ_HOST,'R')
        self.yhz_db_name = self.get_conf(Config.YHZ_DB_NAME,'R')
        # 一生约测试环境物业app
        self.tysy_pro_host = self.get_conf( Config.YSY_PRO_HOST)
        # 一生约正式环境物业app
        self.ysy_pro_user = self.get_conf(Config.YSY_PRO_USER,'R')
        self.ysy_pro_release = self.get_conf(Config.YSY_PRO_HOST,'R')
        # 小猪测试数据库
        self.ysyo2o_host = self.get_conf(Config.O2O_HOST)
        self.tdb_name_o2o = self.get_conf(Config.O2O_DB_NAME)
        # 小猪正式数据库
        self.ysy_o2o = self.get_conf(Config.O2O_HOST,'R')
        self.db_name_o2o = self.get_conf(Config.O2O_DB_NAME,'R')
        # 姐妹邦测试环境
        self.jmb_test = self.get_conf(Config.JMB_T_HOST)
        self.jmb_t_user = self.get_conf(Config.JMB_T_USER)
        # 姐妹邦测试环境DB
        self.jmb_t_db_host = self.get_conf(Config.JMB_T_DB_HOST)
        self.jmb_t_db_name = self.get_conf(Config.JMB_T_DB_NAME)
        self.jmb_t_db_user = self.get_conf(Config.JMB_T_DB_USER)
        self.jmb_t_db_pwd = self.get_conf(Config.JMB_T_DB_PWD)
        self.jmb_t_db_port = self.get_conf(Config.JMB_T_DB_PORT)
        # 建能通測試環境
        self.jnt_app_test = self.get_conf(Config.JNT_APP_TEST)

    def get_conf(self,value, title= 'T'):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        if title == 'T':
            title = Config.TITLE_DEBUG          # 调用类变量
        else:
            title = Config.TITLE_RELEASE
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改：w+ 可读、可写-覆盖写；如无文件则创建
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == "__main__":
    con = Config()
    print(con.yhz_test)
