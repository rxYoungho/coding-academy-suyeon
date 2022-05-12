import py
import pyautogui
import time

# 화면 크기 출력
# print(pyautogui.size()) 

# # 시간차 두기
# time.sleep(2)

# # 마우스의 현재 위치 받기 (x, y)
# # x, y = pyautogui.position()

# pyautogui.moveTo(33, 791, 2) # x, y, duration(float)
# pyautogui.click() #button='left' or 'right'
# pyautogui.doubleClick()

# 마우스 드래그 
# print(pyautogui.position())
# time.sleep(2)
# print(pyautogui.position())
pyautogui.moveTo(355, 122, 2)
pyautogui.dragTo(629, 396, 2, button='left')