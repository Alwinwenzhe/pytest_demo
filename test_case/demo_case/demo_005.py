import time, datetime

def draw_start_enter(start_time,wait_time=9):
    '''判定开始后才进入抽签环节'''
    # 仅显示当前时分
    wait_s = wait_time*60
    while True:
        cur_time = int(time.time())
        else_time = start_time - cur_time
        if else_time < wait_s:
            print('距离抽签时间小于{0}分钟，可开始抽签'.format(wait_time))
            break
        else:
            print("抽签时间未到，请等待30s")
            time.sleep(30)

def join_time(self,hm):
    '''
    将传入小时分钟，转化为时间戳
    :param hm:
    :return:
    '''
    pass

if __name__ == '__main__':
    start_time = time.time()
    # print(start_time)
    # draw_start_enter(1666336815)

    hole_time = "2022-10-21 18:18:18"
    tt = datetime.datetime.strptime(hole_time, "%Y-%m-%d %H:%M:%S")
    un_time = int(time.mktime(tt.timetuple()))
    print(un_time)
