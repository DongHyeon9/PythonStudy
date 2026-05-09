s1=set([1,2,3])
s2={1,2,3}
s3=set('Hello') # 문자열을 set으로 변환 {'H', 'e', 'l', 'o'} : 중복된 문자 'l'은 하나만 포함

# print(s1[0]) # set은 순서가 없어서 인덱싱 불가능

# 요소 추가 add, update
s1.add(4) # set에 요소 추가
s1.update([3,4,5,6]) # 여러 요소를 한 번에 추가

s1.remove(6) # set에서 요소 제거

#집합 연산
s4={1,2,3,4,5}
s5={4,5,6,7,8,9}

# 교집합
print(s4.intersection(s5)) # {4, 5}
print(s4 & s5) # {4, 5}

# 합집합
print(s4.union(s5)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s4 | s5) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
print(s4.difference(s5)) # {1, 2, 3}
print(s4 - s5) # {1, 2, 3}
