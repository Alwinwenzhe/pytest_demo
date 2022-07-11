# -*- coding: utf-8 -*-


"""
封装log方法

"""

import logging
import os
import time

#定义字典数据
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    '''处理文件及文件夹'''
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    '''日志写入文件位置位置'''
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)        # 向此日志记录器添加指定的处理程序(error日志)。
    logger.addHandler(MyLog.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)     # 从此记录器中删除指定的处理程序。
    logger.removeHandler(MyLog.handler)


def get_current_time():
    return time.strftime(MyLog.date, time.localtime(time.time()))


class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    #  工程根目录
    log_file = path+'/Log/log.log'
    err_file = path+'/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.INFO))      # 设置此日志记录器的日志级别。等级必须是int或str。
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file, encoding='utf-8')       # 一个处理程序类，它将格式化的日志记录写入磁盘文件。
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod       # 静态方法无需实例化;也可以实例化后调用
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)    # Log 'msg % args' with severity 'DEBUG'.
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')


if __name__ == "__main__":
    MyLog.debug("This is debug message")        # 未实例化调用静态方法
    MyLog.info("This is info message")
    MyLog.warning("This is warning message")
    MyLog.error("This is error")
    MyLog.critical("This is critical message")
    mylog = MyLog()                            # 实例化之后再调用
    print(mylog.path)

