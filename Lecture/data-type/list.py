odd = [1, 3, 5, 7, 9]
# 리스트이름 = [element1, element2, element3, element4] -> 요소 => element

# 여러가지 리스트의 생김새
a = [] # empty list
b = [1, 2, 3] # integer를 포함한 리스트
c = ["Life", "is", "too", "short"] # string을 포함한 리스트
d = [1, 2, "Life", "is"] # string & ingeter을 포함한 리스트
e = [1, 2, ["Life", "is"]] # integer, list를 포함한 리스트 
f = [1,2,[3,4,[5,6,[7]]]]
# 리스트의 인덱싱
print(b[1]) # 2
print(b[-1]) # 3
print(e[2]) # ["life", "is"]

print(b[0] + b[2])
print(e[2][0]) # 2d
print(e[2][-1]) # 2d
print(f[2][2][0]) # 3d
print(f[2][2][2][0]) # 4d

# 리스트의 슬라이싱 
a = [2,4,6,8,10]
print(a[1:4]) # 2, 3, 4
b = a[1:4]
print(b)
print(a[:3]) # [요건 그자리:요건 그 전자리]

# 중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5] # 2d
# [3, ['a', 'b', 'c'], 4,]
print(a[2:5])
# ['a', 'b']
print(a[3][:2]) # 구우우웃

# 리스트 더하기 Concatenation
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1,2,3,4,5,6]

# 리스트 반복하기
a = [1,2,3]
print(a*5)

# 리스트 길이 구하기
a = [1,2,3,4,5,1,2,2,5,12,1,23,1]
print(len(a))

# a = [1,2,3] # list
# b = "4, 5, 6" # string
# print (a+b) # [1,2,3] 4,5,6 -> 절대 안됨

# 리스트에서 값 수정하기
a[3] = 7
print(a)

# del 함수를 사용하여 리스트 element 삭제하기
del a[3]
print(a)

#⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️ 리스트 관련 함수들 ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
# 리스트에 element 추가하기 (append) # append의 특징상 항상 맨 뒤에 추가 됩니다.
a = [1,2,3,4]
a.append(5)
print(a)

a.append([5,6])
print(a)

# 정렬 SORT !!!! 🔥 -> 효율성 
a = [1,4,3,2,7,5]
a.sort()
print(a)

# 리스트 뒤집기 (reverse)
a = [6,5,4,3,2,1]
a.reverse()
print(a)

# 위치 반환 index
a = [6,5,4,3,2,1,"a"]
print(a.index(6)) # 6이라는 숫자를 가진 element는 몇번쨰에 있냐? 
location = a.index("a") # a의 인덱스 = 6 목적: 스트링을 지우는것 
del a[location]
print(a)

# 리스트에 element insert 삽입
a = [1,2,3]
a.insert(3,"abc")
print(a)

# 리스트 요소 제거 (remove)
a = [1,2,3,1,2,3]
a.remove(3) # 첫번째 값만 지움 
print(a) 

# 리스트 요소 끄집어내기 (pop)
a = [1,2,3]
print(a.pop(1)) # index
print(a)

# 리스트에 포함된 element 개수 세기 
a = [1,2,3,4,5,6,1,2,1,1]
print(a.count(1))


# 연습문제 1 (2:10초)
# 홍길동씨의 주민번호는 961105-1234567이다. 홍길동 씨의 주민등록번호를 연월일(YYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자!
# 슬라이싱 사용

# 연습문제 2 
# [1,2,5,4,3] 리스트를 [5,4,3,2,1]로 만들어 보자.
# 
a.sort()
a.reverse()
print(a)

# 연습문제 3
# 홍길동씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해라
# 국어: 80
# 수학: 55
# 영어: 75

