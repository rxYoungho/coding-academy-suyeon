# """
# while문의 기본 구조!

# while <조건문>:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3

# <조건문>이 참인경우에 indentation된 수행 문장들을 행 하라.

# GUI -> Graphic User Interface
# """

# # 열 번 찍어 안 넘어가는 나무 없다
# treeHit = 0 
# # 나무를 열 번 찍을때까지 아래 문장들을 반복해라!
# while treeHit < 10:
#     treeHit = treeHit + 1 # Hit tree 
#     print("나무를 %d번 찍었습니다." %treeHit)
#     if treeHit == 10:
#         print("나무가 넘어 갔습니다.")

# """
# treeHit: 0 | 조건문 참 | treeHit == 0 | 
# """

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# ...
# Enter number: """

# number = 0
# # number가 4가 될 때 까지 아래 문장들을 반복해라!!!
# while number != 4:
#     print(prompt)
#     number = int(input())
#     print("당신은 다음과 같은 숫자를 입력하였습니다: %d" % number)

# # 밥을 세 번 먹었다면 굶어라 아니면 밥을 세 끼를 무조건 먹어라 
# # while문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합을 구하라
# # 1부터 100까지 더하시오

# count = 0
# tot = 0
# while count < 100:
#     tot = tot + count 
#     """
#     0 = 0 + 0
#     0 = 0 + 1
#     1 = 1 + 2
#     3 = 3 + 3
#     6 = 6 + 4
#     10 = 10 + 5
#     15 = 15 + 6
#     """
#     count = count + 1
#     if count == 100:
#         print(tot)


# # while문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합을 구하라
    
#     count = 0 # 1부터 1000까지의 자연수
#     tot = 0
#     while count < 1000:
#         # 3의 배수의
#         if count % 3 == 0:
#             tot = tot + count # 합을 구하라 
#         count = count + 1
#     print(tot)


# # status = ""
# # while True:
# #     if status == "Error":
# #         break

# coffee = 10
# money = 300 
# while money == 300: 
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1 
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break # while문을 나가라!

## while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1 
    if a % 2 == 0: 
        continue
    print(a)

"""

while문을 사용하여 다음과 같이 별을 표시하는 프로그램을 작성하자.

*
**
***
****
*****

"""
count = 0
while count < 5:
    count += 1
    print("*" * count)

