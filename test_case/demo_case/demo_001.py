import cv2, pyautogui, time

sour_home = cv2.imread(r'../../pic/xj/stu/001_pc_home.png')
goal_img_path = cv2.imread(r'../../pic/xj/stu/001_pc_home_stu_client.png')
# 目标截图
goal_pic = cv2.imread(goal_img_path)
sour = cv2.imread(sour_home)
# 读取目标截图的高\宽
heigh,width,channel = goal_pic.shape
# 进行模板的匹配,最后的参数就是匹配方法
result = cv2.matchTemplate(sour,goal_pic,cv2.TM_SQDIFF_NORMED)
# 解析匹配区域左上角坐标,返回四个坐标
for i in range(4):
    print("正在点击第{0}个点".format(i+1))
    loc = cv2.minMaxLoc(result)[i]
    print(loc)
    time.sleep(3)
