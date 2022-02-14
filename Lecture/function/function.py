"""
함수를 왜 쓸까?
    1. 입력대비 항상 다른 아웃풋을 얻기위해
    2. 반복을 없애기 위해
    3. 더 직관적으로 코드를 작성하기 위해서 

def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...

"""
# 이 함수의 이름은 add이고 입력으로 2개의 x,  y값을 받으며, 결괏값은 2개의 입력값을 더한 값이다. 
def add(x, y): # 매개변수 -> Parameter
    result = x + y
    return result

c = add(12312, 123) # 인자 -> Argument
print(c)


def waterFlush(start):
    water = 1 # True
    if start == True:
        water = 1
        return water
    else:
        water = 0
        return water

def spin(start):
    roll = 1
    if start == True:
        roll = 1
        return roll
    else:
        roll = 0
        return roll

def soap(start):
    soapStart = 1
    if start == True:
        soapStart = 1
        return soapStart
    else:
        soapStart = 0
        return soapStart

start = 1
waterFlush(start)
spin(start)
soap(start)
"""
빨래 하는 기계
1. 물이 나와야 함 -> 함수 (시작버튼)
    -> 시작 버튼을 누르면 물이 나와야함
2. 돌아가야 함 -> 함수
    -> 시작 버튼을 누르면 돌아가야 함
3. 세재도 자동으로 넣어줘야함 -> 함수
    -> 시작 버튼을 누르면 돌아가야 함
"""


# 매개변수 즉 입력값이 없는 함수
def dannySam():
    return "네" # String 

answer = dannySam()

# Return값이 즉 결과값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(15, 52)