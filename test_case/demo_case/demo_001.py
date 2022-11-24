import cv2, pyautogui, time

if __name__ == '__main__':
    list_a = [1,2,3,4,6]
    for k,v in enumerate(list_a):
        if k == len(list_a)-1:
            print(v)