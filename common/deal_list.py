# -*- coding:utf-8 -*-
# Status:
# Time:

class DealList(object):

    def list_last(self,list_a,end_loa):
        '''执行list中某些元素知道倒数第几个停止'''
        for k, v in enumerate(list_a):
            if k == len(list_a) + end_loa:
                break