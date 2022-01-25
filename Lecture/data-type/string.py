"""
String, 문자열이란, 단어 등으로 구성된 문자들의 집합을 의미한다.

"Life is too short, You need Python"
"a"
"1234"
'Python is fun'

"""

# 문자열에 작은따옴표 (') 포함시키기
from audioop import mul


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
print(a[0]) # index
print(a[1]) # index
print(a[-1]) # 맨 뒤꺼
print(a[-2]) # a
print(a[-0]) # 그대로 W

print(a[0:5]) 
print(a[4:4]) # 안나옵니다.

