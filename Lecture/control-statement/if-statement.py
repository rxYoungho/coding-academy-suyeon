"""
Why if statement?

"돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다."

"If you have money, take taxi else walk"

"수학이 100점이 나오면 컴퓨터를 사주고, 100점이 안나오면 혼날거야"

"""

math_point = 100

if math_point == 100:
    print("컴퓨터를 사줄거야")
else:
    print("혼남")

"""
# if 문의 기본 구조

if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B

# 들여쓰기
if 조건문:
    수행할 문장1
수행할 문장2
"""

money = True
if money == True:
    print("택시를")
    print("타고")
    print("가라")

"""
# 비교 연산자 
x < y
x > y
x >= y : x is greater than or equal to y
x <= y : x is less than or equal to y
x == y : 같다 
x != y : 같지 않다
"""
x = 2
y = 3
print(x != y)


"만약 3000원보다 많이 있으면 택시를 타고 가고, 아니면 걸어가라"
money = 3000
if money > 3000:
    print("TAXI")
else: 
    print("walk")

"""
# 다른 연산자들
or
and
not

x or y : x와 y 둘중에 하나만 참이여도 참이다
x and y: x와 y 둘 다 참이여야만 참이다.
not x: x가 거짓이면 참이다 

"돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
"""

"""
1 in [1,2,3] -> "1이 [1,2,3]에 있나요?" -> "is 1 in [1,2,3]" -> True
1 not in [1,2,3] -> "1이 [1,2,3]에 없나요?" -> is 1 not in [1,2,3] -> False

'a' in ['a','b','c'] -> True
'a' in ('a','b','c') -> True
'a' not in ('a','b','c') -> False 
"""
# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("Taxi")
else:
    print("Walk")

# 주머니에 돈이 있으면 가만히 있고, 돈이 없으면 카드를 꺼내라"
pocket = ['money', 'paper', 'cellphone']

if 'money' in pocket:
    pass # 가만히 있겠다.
else:
    print("카드를 꺼내라 ")


# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 만약 카드가 있으면 지하철을 타고, 돈도 없고 카드도 없으면 걸어 가라.

pocket = ['paper', 'cellphone', 'card']

if 'money' in pocket:
    print("택시타")
else:
    if 'card' in pocket:
        print('지하철 타')
    else: 
        print("걸어가")

# elif
pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
    print("taxi")
elif 'card' in pocket:
    print("Metro")
else:
    print("Walk")

# 책상위에 연필이 있으면 공부를 하고, 연필이 없고 지우개가 없으면 잠을 자고, 연필은 있지만 노트북이 없으면 공부하고, 셋 다 없으면 게임해라.

desk = ['pencil']

if 'pencil' in desk:
    print("Study")
elif 'eraser' in desk:
    print("Sleep")
elif 'pencil' in desk and 'laptop' not in desk:
    print("Study")
else:
    print("game")

# 조건부 표현식
score = 60
if score >= 60:
    message = "Success"
else:
    message = "Failure"

print(message)

message = "success" if score >= 60 else "failure"
print(message)


a = "Life is too short, you need python"

if 'wife' in a: print("wife")
elif 'python' in a and 'you' not in a: print("Python")
elif "shirt" not in a: print("Shirt")
else: print("none")

