import cv2
import numpy as np

img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/white.png')

# cv2.line(img, (50, 50), (150,50), (255, 0, 0)) # 파란색 1픽셀짜리 선

# cv2.line(img, (100, 100), (400, 100), (255, 255, 0), 10) # 10필셀 두깨의 선

# cv2.line(img, (100, 350), (400, 400), (0,0,255), 20, cv2.LINE_4)

# cv2.line(img, (100, 450), (400, 500), (0,0,255), 20, cv2.LINE_AA) 

# cv2.rectangle(img, (50,50), (300,150), (255,0,0), 10) 

# cv2.rectangle(img, (50,350), (300,150), (255,0,0), -1) 

# 다각형 그리기
#번개모양 선 좌표
# pts1 = np.array([[50,50], [150,150], [100, 140], [200,240]], dtype = np.int32)
# pts2 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype = np.int32)


# # parameter : (img, points, isClosed, color, thickness, lineType)
# cv2.polylines(img, [pts1], True, (255,0,0)) # 번개모양
# cv2.polylines(img, [pts2], True, (0,0,0), 5, cv2.LINE_AA) # 5각형

# img = cv2.imread(img)
# title = "IMG"
# x, y = 100, 100

# while True:
#     cv2.imshow(title, img)
#     cv2.moveWindow(title, x, y)
#     key = cv2.waitKey(0) & 0xFF
#     print(key, chr(key))

#     if key == ord('w'):
#         y -= 10
#     elif key == ord('s'):
#         y += 10
#     elif key == ord('a'):
#         x -= 10
#     elif key == ord('d'):
#         x += 10
#     elif key == ord('q'):
#         break
#     cv2.destroyAllWindows()
#     cv2.moveWindow(title,x,y)

# 마우스 이벤트로 동그라미 그리기 
cv2.imshow('title', img)

colors = {
    'black':(0,0,0),
    'red':(0,0,255),
    'blue':(255,0,0),
    'green':(0,255,0)
}

def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)
    color = colors['black']
    print(cv2.EVENT_FLAG_CTRLKEY)
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['green']
    
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['blue']
        
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']
        
        cv2.circle(img, (x,y), 30, color, -1) # 지름이 30픽셀인 검은색 원을 해당 좌표에 그림
        cv2.imshow('title', img)

cv2.setMouseCallback('title', onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break 

cv2.destroyAllWindows()

