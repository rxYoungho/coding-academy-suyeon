import cv2

# 1. 이미지 파일을 화면에 표시
#표시할 이미지의 경로
# img_file = "/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/지코1.jpg"
# img = cv2.imread(img_file) # 이미지를 읽어서 img 변수에 할당 

# cv2.imshow('지코', img) # 읽은 이미지를 화면에 표시

# cv2.waitKey() #아무키나 입력될 때 까지 대기
# cv2.destroyAllWindows() # 창 모두 닫기 

# 2. 이미지 파일을 그레이스케일로 변환
# img_file = "/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/지코1.jpg"
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

# cv2.imshow('IMG', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 3. 원본 (컬러) 이미지를 그레이스케일된 이미지로 저장
# img_file = "/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/지코1.jpg"
# save_file = "/Users/Danny/Desktop/grayscale.jpg"

# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# cv2.imshow("ZICO", img)
# cv2.imwrite(save_file, img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 4. 동영상 및 카메라 프레임 읽기 
# video_file = "/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/test.mp4"
# cap = cv2.VideoCapture(video_file)

# while True:
#     _, img = cap.read() # return ret=False or True, img=3Dimensional array
#     cv2.imshow("비디오", img)
#     cv2.waitKey(25) # 25ms, 40fps 

# cap.release()
# cv2.destroyAllWindows()

# 5. 동영상 프레임 읽기 

# cap = cv2.VideoCapture(0) # 0번 카메라 장치 연결

# while True:
#     ret, img = cap.read()
#     cv2.imshow('camera', img)
#     if cv2.waitKey(1) != -1: # 아무 키나 누르면
#         break

# cap.release()
# cv2.destroyAllWindows()

# 6. 카메라로 사진 찍기
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('camera', frame)
#     if cv2.waitKey(1) != -1:
#         cv2.imwrite('/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/photo.jpg', frame)
#         break
# cap.release()
# cv2.destroyAllWindows()

# 7. 카메라로 녹화하기
cap = cv2.VideoCapture(0)

file_path = "/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/computer-vision/record.mp4"
fps = 25.40
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 MJPG, DIVX 등등 
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (int(width), int(height))
out = cv2.VideoWriter(file_path, fourcc, fps, size)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    out.write(frame) # 파일 저장
    if cv2.waitKey(1) != -1: # 아무키나 눌렀을때
        break

out.release()
cap.release()
cv2.destroyAllWindows()
