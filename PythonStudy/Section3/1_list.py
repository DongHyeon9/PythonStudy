# 리스트(List) : 여러 개의 데이터를 하나의 변수에 저장하는 자료형
l1=[10,3.4,'ABC',True]

# tuple : 요소의 값을 변경할 수 없는 자료형
t1=(10,3.4,'ABC',True)

# set : 중복된 요소를 허용하지 않는 자료형
s1={10,3.4,'ABC',True}

# dictionary : 키(key)와 값(value)으로 이루어진 자료형
d1={'name':'John', 'age':30, 'city':'New York'}

l1.append(20) # 리스트에 요소 추가
# t1.append(20) # 튜플은 요소 추가 불가능
s1.add(20) # 세트에 요소 추가
d1['country']='USA' # 딕셔너리에 요소 추가

print(l1) # [10, 3.4, 'ABC', True, 20]
print(t1) # (10, 3.4, 'ABC', True)
print(s1) # {10, 3.4, 'ABC', True, 20}
print(d1) # {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

st=dir(bool) # dir메소드는 list의 형태로 반환

import glob
files=glob.glob('../*.py',recursive=True) # 상위폴더에서 재귀적으로 .py 파일을 리스트로 반환
print(files) 

from re import L
import subprocess
subprocess.run(['notepad.exe','a.txt']) # notepad.exe를 실행할 때 인자로 a.txt를 전달 (리스트 형태로 전달)

l2 = list() # list를 명시적으로 생성
# Iterable한 객체를 리스트로 변환
l3 = list('ABCDEFG') # 문자열을 리스트로 변환 ['A', 'B', 'C', 'D', 'E', 'F', 'G']
l4 = list(range(10)) # range 객체를 리스트로 변환 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# generator expression
l5 = list((i for i in range(10) if i%2==0)) # generator expression을 리스트로 변환 [0, 2, 4, 6, 8]
l6=list(i for i in range(10) if i%2==0) # generator expression을 리스트로 변환 [0, 2, 4, 6, 8] (괄호 생략 가능)

# []표기법 사용
l7=[] # 빈 리스트 생성
l8 = [1,3.4,'AAA',[3,4,5]]  # 리스트 안에 리스트도 가능 (중첩 리스트)

# list comprehension
# 리스트를 생성하는 간결한 방법
l9 = [i for i in range(10) if i%2==0] # 0부터 9까지의 숫자 중에서 짝수만 리스트로 생성 [0, 2, 4, 6, 8]

# 2중 for문을 이용한 리스트 컴프리헨션 [['A', '1'], ['A', '2'], ['B', '1'], ['B', '2']]
s1='AB'
s2='12'
l10=[[v1,v2] for v1 in s1 
             for v2 in s2]

# indexing과 slicing
l11=[1,2,3,[4,5,6]]
print(l11[0]) # 1
print(l11[-1]) # [4, 5, 6]
print(l11[-1][0]) # 4

l12=[0,1,2,3,4,5,6,7,8,9]

print(l12[1:3]) # [1, 2]
print(l12[1:9:3]) # [1, 4, 7]

sc=slice(1,9,3) # slice 객체 생성
print(l12[sc]) # [1, 4, 7]

# unpacking
l12 = [1,'AB',[7,8,9]]

a,b,c = l12 # 리스트의 요소를 각각 변수에 할당

print(f'{a}, {b}, {c}') # 1, AB, [7, 8, 9]

#a,b= l12 # ValueError: too many values to unpack (expected 2) 리스트의 요소가 3개인데 변수는 2개이므로 언패킹 불가능
#a,b,c,d = l12 # ValueError: not enough values to unpack (expected 4, got 3) 리스트의 요소가 3개인데 변수는 4개이므로 언패킹 불가능

l13 = [0,1,2,3,4,5,6,7,8,9]

print(len(l13))

del l13[0] # 리스트의 첫 번째 요소 삭제 [1, 2, 3, 4, 5, 6, 7, 8, 9]
del l13[1:9:3] # 리스트의 1,4,7 번째 요소 삭제 [1, 3, 4, 6, 7, 9]

# append, insert, extend
l14 = [1,3,5]
l14.append(7) # 리스트의 마지막에 요소 추가 [1, 3, 5, 7]
l14.insert(1,2) # 리스트의 1 번째 인덱스에 요소 추가 [1, 2, 3, 5, 7]
l14.extend([8,9]) # 리스트의 마지막에 여러 요소 추가 [1, 2, 3, 5, 7, 8, 9]    l14+=[8,9]와 동일
l14.append([10,11]) # 리스트의 마지막에 리스트 추가 [1, 2, 3, 5, 7, 8, 9, [10, 11]]

# remove, pop
l15 = [1,2,3,4,5,3]
del l15[0] # 리스트의 첫 번째 요소 삭제 [2, 3, 4, 5, 3]
l15.remove(3) # 리스트에서 값이 첫번째 3을 삭제 [2, 4, 5, 3]

n=l15.pop() # 리스트의 마지막 요소를 반환하고 삭제 [2, 4, 5] 반환값: 3

# count, index
l16 = [1,2,3,4,5,6,7,8,9]
print(l16.count(3)) # 리스트에서 3의 개수 반환 1
print(l16.index(3)) # 리스트에서 3의 인덱스 반환 2
print(l16.index(3,3)) # 리스트에서 3의 인덱스를 3 번째 인덱스부터 검색하여 반환 -1 (찾는 값이 없으면 -1 반환)
print(l16.index(3,0,5)) # 리스트에서 3의 인덱스를 0 번째 인덱스부터 5 번째 인덱스까지 검색하여 반환 2
#print(l16.index(10)) # ValueError: 10 is not in list

# sort, reverse
l17 = [6,4,8,2,1,3,9,7,5]
l18=sorted(l17) # 리스트를 정렬하여 새로운 리스트 반환 [1, 2, 3, 4, 5, 6, 7, 8, 9]
l17.sort() # 리스트를 정렬하여 원본 리스트를 변경 [1, 2, 3, 4, 5, 6, 7, 8, 9]
l18.reverse() # 리스트를 역순으로 변경 [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 깊은 복사, 얕은 복사
# 얕은 복사 시 내부의 list객체가 변경되면 다른 복사본에서도 변경이 일어남
l19=[1,2,[3,4]]
l20=l19 # l19와 l20은 같은 리스트를 참조 (얕은 복사)
l21=l19.copy() # l19와 l21은 다른 리스트를 참조 (얕은 복사)

import copy
l22=copy.deepcopy(l19) # l19와 l22는 다른 리스트를 참조 (깊은 복사)