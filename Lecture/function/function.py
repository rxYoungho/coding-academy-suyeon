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


# Return값이 즉 결과값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(15, 52)

# 입력값도 없고 결과값도 없는 함수
def dannySam2():
    print("네")

answer = dannySam() # "네"

answer2 = dannySam2()
print(answer2)

# 매개변수 지정하여 호출하기
def add(abc,defg):
    return abc+defg 


result = add(defg = 300, abc = 128)
result2 = add(abc = 1, defg = 400)
print(result, result2)


def add_many(*args):
    print("args:", type(args))
    result = 0
    for i in args:
        result = result + i
    return result 

result = add_many(1,2,3,4,5,6,7,8,9,10)
result2 = add_many(3,6,9,12)
print(result, result2)

def add_mul(choice, *args):
    print("args:", args)
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result 

add_mul("add", 1,2,3,4,5,6,7,8,9,10)


# 주어진 자연수가 홀 수인지 짝수인지 판별해주는 함수 (is_odd)를 작성해 보자! 

# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자! (단 입력드로 들어오는 수의 개수는 정해져 있지 않다.)
# 평균값을 구할때 len함수 사용 할 것! 

# 함수의 결괏값은 항상 하나이다.

def add_and_mul(a,b):
    return a+b, a*b
result_add, result_mul = add_and_mul(7,9)
print(result_add)
print(result_mul)


def say_nick(nick):
    if nick == "바보":
        return 
    print("나의 별명은 %s 입니다." % nick)

say_nick("야호")
say_nick("바보")


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old=20, man=True):
    print("my name is %s" % name)
    print("my age is %d." % old)
    if man:
        print("I am Man")
    else:
        print("I am Woman")

say_myself("Suyeon", 18, False)
say_myself(man = False, name = "Suyeon", old = 18)
say_myself(name="Suyeon", old = 18, man = False)
say_myself(name="Danny")


# SCOPE 범위 
a = 1 
def vartest(a):
    a = a + 1

print(vartest(a))
print(a)

a = 1
def vartest2():
    global a # 함수안에서 외부에 존재하는 변수를 선택
    a = a + 1

vartest2()
print(a)



a = [1,2,3,4,5,6,7,8,9,10]
tot = sum(a)
print(tot)