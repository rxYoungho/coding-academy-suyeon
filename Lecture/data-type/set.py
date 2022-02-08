# 집합의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다 (Unordered)


"""
list = [1,1,1,1,1,1,1,2,3,4,5,6,6,6,6,6,7,8,9]
[1,2,3,4,5,6,7,8,9] -> duplicate을 없애고 싶어!!
set(list)
"""

s1 = set([1,2,3])
l1 = list(s1)
print(l1[0])

t1 = tuple(s1)
print(t1[0])

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 -> & -> And
print(s1 & s2)
print(s1.intersection(s2))
# 합집합 -> | -> Or 
print(s1 | s2)
print(s1.union(s2))
# 차집합 -> -
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

# 집합과 관련된 함수들
# 값을 추가하는 add
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 (Update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기 (Remove)
s1 = set([1,2,3])
s1.remove(3) # element 값
print(s1)

