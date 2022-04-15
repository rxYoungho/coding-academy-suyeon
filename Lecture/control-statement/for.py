

# """
# for문의 기본 구조

# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...
# """

# # 반복문
# test_list = ['one','two','three']
# for i in test_list:
#     print(i)

# # 1부터 10까지 들어있는 리스트를 전부 출력하시오 (for문을 사용해서)

# # 다양한 for문의 사용
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first, last)
        
# """
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고
# 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.

# Process
# 1. 총 5명의 학생들의 점수가 달린 리스트가 주어진다.
# 2. 각각의 점수를 확인하여 60점이 넘으면 합격
# 3. 각각의 점수를 확인하여 60점이 못 넘으면 불합격

# """
# score = [1,2,3,4,61]
# for i in score: 
#     if i >=60:
#         print("합격")
#     else:
#         print("불합격")

# """
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점을 가장 빨리 넘긴 학생을 뽑으시오.
# """
# scores = [90,25,67,45,80]
# for score in scores:
#     if score < 60:
#         continue
#     print("축하합니다 당신의 점수는: ", score)

# a = range(10)
# print(a)

# a = range(1,11)
# print(a)

# add = 0
# for i in range(1, 11):
#     add = add + i
# print(add)



# scores = [90, 25, 67, 45, 80]
# for i in range(len(scores)): # 0, 1, 2, 3, 4
#     if scores[i] < 60: # indexing
#         continue
#     print("축하합니다 당신의 점수는:", scores[i])


# # 2단 루프 2D -> Nested For Loop
# for i in range(2,10): # 2단부터 9단
#     for j in range(1,10): #2x1 ~ 2x9
#         print(i, "x", j, ":",i * j)
#     print("")

# # 리스트 Comprehension 사용하기
# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
# print(result)


# # 이거 쓰면 ㄹㅇ 고수 
# a = [1,2,3,4]
# result = [num * 4 for num in a]
# print(result)

# # 짝수에다가만 3을 곱하여 result로 출력해라
# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
    
# print(result)

# # 아래랑 동일 한 코드
# for num in a:
#     if num%2==0:
#         result.append(num * 3)

# # 찐 고수 인정하는 코드
# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)
# # result [ 1, 6, 3, 12]

# """
# [ONE LINED CODE!!]

# [표현식 for 객체 in 반복가능객체 if 조건문]
# [num * 3 for num in a if num % 2 == 0]
# """

# # 너무 고수여서 ... 잘 안쓰게 됨 ㅠㅠ 
# result = [x * y for x in range(2,10)
#             for y in range(1,10)]

# print(result)


# """
# 연습문제
# 1. for문을 사용해서 1 부터 100까지의 숫자를 출려하시오.

# 2. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#     ls = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#     for문을 사용하여 A 학급의 평균 점수를 구해 보자.
#     합계 !!

# 3. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드가 있다. list comprehension으로 바꿔라!
# """
# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)


"""


"""
# for x in range(0, 100):
#     print(x)

# people = ['Dave', 'Danny', 'Suyeon', 'DY','Dave', 'Danny', 'Suyeon', 'DY','Dave', 'Danny', 'Suyeon', 'DY']
# for name in people:
#     print(name)

# # people = ['Dave', 'Danny', 'Suyeon', 'DY','Dave', 'Danny', 'Suyeon', 'DY','Dave', 'Danny', 'Suyeon', 'DY']
# # people2 = ['Daze', 'Danny', 'Suyong', 'DN','Dave', 'Danny', 'Suyeon', 'DY','Dave', 'Danny', 'Suyeon', 'DY']

# # for i, each in enumerate(people):
# #     if each != people2[i]:
# #         print(people2[i])

# # # while ~하는 동안에
# # count = 0
# # while count < 100:
# #     print(count)
# #     count = count + 1

# index = 0
# while index < len(people):
#     print(people[index])
#     index += 1

