# Tuple은 리스트와 같은데, 요소들이 삭제, 수정, 생성이 도중에 안된다.
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd')) # 2d matrix 

t1 = (1, 2, 'a', 'b')
print(t1[1:])
print(t1[2])

# Concatenation
t2 = (3,4)
print(t1 + t2)

# 튜플 곱하기
t2 = (3,4)
print(t2 * 4)

# 튜플 길이 구하기
t1 = (1,2,'a','b')
print(len(t1))