"""
파일 열기 모드 
r = 읽기모드 - 파일을 읽기만 할 때 사용 -> 그냥 읽기
w = 쓰기모드 - 파일에 내용을 작성할 때 사용 -> 모두 초기화
a = 추가모드 - 파일의 마지막줄에 새로운 내용을 추가할 때 사용 -> 기존꺼에 추가
"""

# file = open("새파일.txt", 'w') # w means WRITE!!

# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" % i
#     file.write(data)
#     # print("%d번째 줄입니다. \n" % i)
# file.close()

# f = open("/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/input-output/매출액.txt", "r")
# lines = f.readlines() # 전체 뽑아내기: lines = f.read()
# for line in lines:
#     line = line.strip() #줄 끝에 있는 줄 바꿈 문자를 없ㄱ애줌
#     print(line)
# f.close()

# f = open("/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/input-output/새파일.txt", "a")
# data = "\n11번째 줄입니다."
# f.write(data)
# f.close()

with open("/Users/Danny/Desktop/GitHub/coding-academy-suyeon/Lecture/input-output/새파일.txt", "a") as f:
    data = "\n11번째 줄입니다."
    f.write(data)


