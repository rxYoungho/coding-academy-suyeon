# # 변수 -> Variable 
# '''
# 글을 쓰면 이건 Comment라고 합니다.
# '''

# # 정수 -> Integer
# x = 10
# y = 2
# z = 30

# # 문자열 -> String
# tablet = "Ipad"
# phone = "Iphone"
# labtop = "MacBook"
# appleLabtop =  "IMac"

# # 소수 -> Float / Double 
# a = 0.1
# b = 1.1
# c = 1.2312424

# # 주석 -> comment
# # print(tablet)
# # print(phone)
# # print(labtop)
# # print(appleLabtop)

# suyeon = "I"
# verb = "Love"
# noun = "NCT"
# print(suyeon, verb, noun) #아까랑 똑같이 나올것 같다! -> 정답! 

# suyeon = "You"
# verb = "Love"
# noun = "MonstaX"
# print(suyeon, verb, noun)

# suyeon = "She"
# verb = "Likes"
# noun = "Suyeon"
# print(suyeon, verb, noun)

# # 반복문 while  
# num = 0
# while num < 3:
#     print(suyeon, verb, noun)
#     num = num + 1
# print("While문이 끝났습니다.")
# print("num:", num)


#사칙연산
print( 1 + 2 )
print( 3 * 9 )

#변수에 숫자 대입하고 계산하기
a = 1
b = 2
print( a + b )

#변수에 문자 대입하고 출력하기
a = "Python"
print(a)

#조건문
a = 3
if a > 1:
    print("a is greater than 1")

#반복문 for
for a in [1,2,3]:
    print(a)

#반복문 while
i = 0
while i < 3:
    i = i + 1
    print(i)

#함수 
def add(a,b):
    return a + b

print(add(3,4))

#파이썬은 인간다운 언어이다.
if 4 in [1,2,3,4]: print("4가 있습니다.")
