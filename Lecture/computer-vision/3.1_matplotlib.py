import matplotlib.pyplot as plt
import math
import numpy as np 

x = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.25, 3.5, 4.0, 4.5])
y = np.array([0, 0, 10, 40, 70, 80, 100, 100, 100])
plt.plot(x, y, "c")

plt.xlabel("Total rotation speed in seconds")
plt.ylabel("Capture success ratio")

plt.show()
## 다양한 선 스타일 지정
"""
- : 실선
-. : 점 이음선
. : 점
o : 원
^ : 정삼각형
> : 우삼각형
2 : 작은 정삼각형
4 : 작은 우삼각형
p : 오각형
h : 육각형
D : 다이아몬드 표
-- : 이음선
: : 점선
, : 픽셀
v : 역삼각형
< : 좌 삼각형
1 : 작은 역삼각형
3 : 작은 좌 삼각형
s : 사각형
* : 별포
+ : 더하기 표
X : 엑스표
"""
# x = np.arange(10)
# print ( x + 5 )

# f1 = x + 5
# f2 = x ** 2
# f3 = x ** 2 + x*2

# plt.plot(x, 'r--') #빨간색 이음선
# plt.plot(f1, 'g.')
# plt.plot(f2, 'bv')
# plt.plot(f3, 'k--')
# plt.show()

# x = np.arange(10)
# plt.subplot(2, 2, 1) # 2행 2열 중에 첫번째 
# plt.plot(x, x**2)

# plt.subplot(2, 2, 2)
# plt.plot(x, x*5)

# plt.subplot(2,2,3)
# plt.plot(x, np.sin(x))

# plt.subplot(2,2,4)
# plt.plot(x, np.cos(x))

# plt.show()