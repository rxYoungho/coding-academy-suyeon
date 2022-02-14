

"""
for문의 기본 구조

for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
"""

# 반복문
test_list = ['one','two','three']
for i in test_list:
    print(i)

# 1부터 10까지 들어있는 리스트를 전부 출력하시오 (for문을 사용해서)

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first, last)
        
"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고
그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.

Process
1. 총 5명의 학생들의 점수가 달린 리스트가 주어진다.
2. 각각의 점수를 확인하여 60점이 넘으면 합격
3. 각각의 점수를 확인하여 60점이 못 넘으면 불합격

"""
score = [1,2,3,4,61]
for i in score: 
    if i >=60:
        print("합격")
    else:
        print("불합격")

"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점을 가장 빨리 넘긴 학생을 뽑으시오.
"""
scores = [90,25,67,45,80]
for score in scores:
    if score < 60:
        continue
    print("축하합니다 당신의 점수는: ", score)

a = range(10)
print(a)

a = range(1,11)
print(a)

add = 0
for i in range(1, 11):
    add = add + i
print(add)



scores = [90, 25, 67, 45, 80]
for i in range(len(scores)): # 0, 1, 2, 3, 4
    if scores[i] < 60: # indexing
        continue
    print("축하합니다 당신의 점수는:", scores[i])


# 2단 루프 2D -> Nested For Loop
for i in range(2,10): # 2단부터 9단
    for j in range(1,10): #2x1 ~ 2x9
        print(i, "x", j, ":",i * j)
    print("")

# 리스트 Comprehension 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)


# 이거 쓰면 ㄹㅇ 고수 
a = [1,2,3,4]
result = [num * 4 for num in a]
print(result)

# 짝수에다가만 3을 곱하여 result로 출력해라
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    
print(result)