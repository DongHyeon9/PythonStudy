# first class object (일급 객체) 란?
# - 함수의 실제 매개변수가 될 수 있다
# - 함수의 반환 값이 될 수 있다
# - 할당 명령문의 대상이 될 수 있다
# - 동일 비교의 대상이 될 수 있다

def func1():
    print('func1')

def func2(f):
    f()

func2(func1)        # 1. 함수의 매개변수
def func3():
    return func2    # 2. 함수의 반환 값
f=func1             # 3. 할당 명령문의 대상
print(f==func1)     # 4. 동일 비교의 대상

def func4(x):
    return x*x

s1=[1,2,3,4,5]
for i in s1:
    print(i,end=' ')    # 1 2 3 4 5

print()

m=map(func4,s1) # map객체 : 함수, iterable객체 보관

for i in m:     # s1의 요소들을 func4에 보낸 결과 값을 i에 할당
    print(i,end=' ')    # 1 4 9 16 25

s2=list(map(func4,s1))
print(s2)                           # [1,4,9,16,25]
print(list(map(lambda x:x*x,s1)))   # [1,4,9,16,25]
print(list(filter(lambda x:x%2==0,s1)))   # 조건을 만족하는것만 filtering해줌 [2,4]

# 지능형 리스트가 더 편리
s3 = [func4(x) for x in s1]
print(s3)   # [1,4,9,16,25]

# lambda
# 일회용 함수, lambda 매개변수 : 리턴값 의 형태로 사용
s4=['banana','kiwi','apple']
# 객체를 정렬하지 않고 정렬된 객체를 반환
s5=sorted(s4)

print(s4)   #['banana','kiwi','apple']
print(s5)   #['apple','banana','kiwi']

def func5(x):
    return len(x)

# 길이로 정렬
print(sorted(s4,key=func5)) # ['kiwi','apple','banana']
print(sorted(s4,key=lambda x:len(x))) # ['kiwi','apple','banana']
print(sorted(s4,key=len)) # ['kiwi','apple','banana']

# 각 요소의 문자열을 뒤집은걸 정렬 기준으로 사용
print(sorted(s4,key=lambda x:x[-1::-1]))

x = 10
f1=lambda y : x+y
f2=lambda y,x=x : x+y
x=20
print(f1(1))    # 람다는 호출시점이 적용됨 : 21
print(f2(1))    # 디폴트는 람다를 만들때 적용됨 : 11

# lamdb 표현식 if문
# lambda x: exp1 if 조건 else exp2
# exp1 = 참일시 반환, exp2 = 거짓일시 반환
# 삼항연산자처럼 사용할 순 있지만 가독성이 떨어짐
# 이것보다 길어져야하면 함수를 만들어야됨

f3=lambda x,y : x if x>y else y

print(f3(10,5))
print(f3(6,8))