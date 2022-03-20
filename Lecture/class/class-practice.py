
# result1 = 0 
# result2 = 0


# def add1(num):
#     global result1
#     result1 = result1 + num 
#     return result1


# def add2(num):
#     global result2
#     result2 = result2 + num 
#     return result2



# # A = 3
# print(add1(3))

# # B = 7 
# print(add2(4))


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num
        return self.result

# A유저꺼 계산기
cal1 = Calculator()

# B유저꺼 계산기
cal2 = Calculator()

# C유저꺼 계산기
cal3 = Calculator()

#A유저꺼 계산기
print(cal1.add(3))
print(cal2.add(4))