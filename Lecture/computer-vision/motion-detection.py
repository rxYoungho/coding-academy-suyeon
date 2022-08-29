import cv2 
import numpy as np 

thresh = 25
max_diff = 5

a, b, c = None, None, None 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)


if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()

    while ret:
        ret, c = cap.read()
        draw = c.copy()
        if not ret:
            break 
            
        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        diff1 = cv2.absdiff(a_gray, b_gray)
        diff2 = cv2.absdiff(b_gray, c_gray)

        # 스레시 홀드로 기준치 이내의 모션은 무시 
        ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

        # 두 차이에 대해서 AND연산, 두 영상의 차이가 모두 발견이 된 경우 
        diff = cv2.bitwise_and(diff1_t, diff2_t)

        # 노이즈 제거 하기
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

        # 모션이 발생한 픽셀의 개수 판단후에 사각형 그리기
        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > max_diff: 
            nzero = np.nonzero(diff) # 0이 아닌 픽셀의 좌표 얻기 
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0]), max(nzero[1]), max(nzero[0])), (0,255,0), 2)
            cv2.putText(draw, "Motion Detected!", (10,30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,255))
        
        # 컬러와 스레시홀드영상을 송출
        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("motion sensor", stacked)

        # 다음 비교를 위해 영상 순서 정리
        a = b
        b = c 
        if cv2.waitKey(1) & 0xFF == 27:
            break

