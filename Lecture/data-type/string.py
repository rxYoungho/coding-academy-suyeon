"""
String, 문자열이란, 단어 등으로 구성된 문자들의 집합을 의미한다.

"Life is too short, You need Python"
"a"
"1234"
'Python is fun'

"""

# 문자열에 작은따옴표 (') 포함시키기

food = "Python's favorite food is perl"
print(food)

# 문자열에 큰따옴표 (") 포함시키기
say = '"Python is very easy." he says.'

# 백슬래시 (\)를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy. \" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을때
# 줄을 바꾸기 위한 Escape Code \n 삽입하기
multiline = "Life is too short\nYou need python."
print(multiline)

# 연속된 작은따옴표 3개를 이용하여 multiline 만들기
multiline = '''Life is too short
You need python'''
print(multiline)

# 문자열 더해서 연결하기 (Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 곱하기 
a = "Python "
print(a * 3)

# 문자열 곱하기 응용
print("=" * 50)
print("Welcome Suyeon's Calculator Program")
print("Press 'S' to Start Calculator")
print("=" * 50)

# 문자열 길이 구하기
a = "Welcome Suyeon's Calculator Program"
print(len(a)) # length

# 문자열의 인덱싱과 슬라이싱 
# 인덱싱이란 -> 무엇인가를 "가리킨다"
# 슬라이싱이란 -> 무언가를 "잘라낸다"
a = "Welcome Suyeon's Calculator Program"
# print(a[0]) # index
# print(a[1]) # index
# print(a[-1]) # 맨 뒤꺼
# print(a[-2]) # a
# print(a[-0]) # 그대로 W

# print(a[0:5]) 
# print(a[4:4]) 

# print(a[:]) # 전체

# local = "서울특별시 동작구 신대방제2동"
# si = local[0:5]
# gu = local[6:9]
# dong = local[11:]
# print(si, gu, dong)

# Replacement
# immutable 
local = "서울동시흥동" # -> 서울시 시흥동
print(local[2])

new_local = local[:2] + "시 " + local[3:]
print(new_local)

"현재 온도는 18도 입니다."
"현재 온도는 20도 입니다."
"현재 온도는 30도 입니다."

# 문자열의 대입 (Formatting)
degree = 19
print("현재 온도는 %d도 입니다." % degree) # d = digit

count = "다섯"
print("저는 %s조각의 피자를 먹었습니다." % count) # s = string

print("오늘의 기온은 %d도이고, 저는 너무 추워서 피자를 %s조각을 먹었어요." % (degree, count))

"""
%d = integer
%s = string
%f = floating point (소수)
%c = 문자 
"""
# %표기법
print("Error is %d%%" % 98)

f = 3.42134234
print("%0.4f" % f)

# Format 함수를 이용한 포매팅
print("I eat {number} apples and I love {firstName} {lastName}.".format(number = "five", firstName = "Danny", lastName = "Kim"))

# 왼쪽 정렬
print("{0:<50}".format("HI"))
# 가운데 정렬
print("{0:^50}".format("HI"))
# 오른쪽 정렬
print("{0:>50}".format("HI"))

# f 문자열 포매팅 
name = "김수연"
age = 18
print(f"나의 이름은 {name}입니다. 저는 내년에 {age+1}살이 됩니다.")

# 문자 개수 세기 (count)
stringValue = "nakjwdnajksbbb b b bbbdnajwndaaaadbarbsdfgrgfgdfgdfgaaa a  z aaaaaaaasdasdasdasdasdasdaaa a a  aaajksdniawndkam"
print("stringValue의 개수는: ", len(stringValue)) # length = len
numberOfas = stringValue.count('a')
numberOfbs = stringValue.count('b')
print(numberOfas + numberOfbs)

# 문자의 위치 알려주기 find & index (index를 알고싶어!)
print(stringValue.find('gaaa '))
print(stringValue[51:56])

# 문자열 삽입 (join)
print(",".join('ABC'))

# 문자열 대문자 & 소문자
print(stringValue.upper())
upperStringValue = "NAKJWDNAJKSBBB B B BBBDNAJWNDAAAADBARBSDFGRGFGDFGDFGAAA A  Z AAAAAAAASDASDASDASDASDASDAAA A A  AAAJKSDNIAWNDKAM"
print(upperStringValue.lower())

text = "                         안녕하세요, 저는 김영호입니다. 이번 프로젝트의 과제는                   "
#왼쪽 공백 지우기
print(text.lstrip())
#오른쪽 공백 지우기
print(text.rstrip())
#양쪽 공백 지우기
print(text.strip())

# 문자열 바꾸기 (Replace)
a = "Life is too short"
print(a.replace("Life is", "You are"))

# 문자열 나누기 (split)
a = "단편소설(短篇小設)은 일반적으로 대한민국에서는 200자 원고지 150매 이내의 소설을 말한다. 문학동네에서는 80매 이상 200매 이하를 기준으로 하며, 조금이라면 부족하거나 넘쳐도 크게 신경쓰지 않는다고 한다. 단편소설 공모전의 경우 원고지 70~100매 사이를 요구하기도 한다."
words = a.split()

b = "a:b-c-d"
print(b.split("-"))

