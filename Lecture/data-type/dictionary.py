# Hash // Dictionary

# {Key1:Value1, Key2:Value2, Key3:Value3}

dic = {'Apple':'A fruit with red and green color', 'Banana':'a fruit with yellow color', 'cat':'an ailen'}

# dictionary 호출 // Value 변경
dic['Apple'] = "A fruit with white color"
print(dic['Apple'])

# dictionary key and value 추가하기
dic['dog'] = "a cute animal"
print(dic)

# dictionary 생성 
a = {1:'a'} 
print(a)

b = dict()
print(b)

# dictionary에 값 집어넣기
a[2] = 'b'
a[3] = 'c'
a[6] = 'f'
a[7] = [1,2,3,4]
print(a)

del a[1]
del a[7]
print(a)

# 관련 된 함수들
# Key 리스트 만들기 
print(list(dic.keys()))

# Key 나열해보기
for key in dic.keys():
    print(key)

# Value 리스트 만들기
print(list(dic.values()))

# 전부 얻기
print(dic.items())

# # 전부 지우기
# dic.clear()
# print(dic)

# Key를 통해서 Value 얻기
print(dic.get('Apple'))
print(dic.get('Banana'))

# 우리가 찾고자 하는 Key 딕셔너리에 있는지 확인하고 싶을때
print('human' in dic)
