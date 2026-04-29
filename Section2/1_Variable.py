import sys
import ctypes

n=10
f=3.4

print(n)
print(hex(id(n)))   #객체의 주소 출력

print (sys.getrefcount(n))  #객체의 참조계수 출력

print(sys.getsizeof(n))     # 객체의 메모리 크기
print(sys.getsizeof(f))

print(type(n))              # 객체의 타입 이름 출력
print(isinstance(n,int))    # 객체의 타입 확인 (True or False)
print(isinstance(f,int))
print(type(n) is int)



print('===== ==연산자 vs is 연산자 =====')
s1 = 'To Be Or Not To Be'
s2 = s1

s3='To Be Or Not To'
s3=s3+' Be'

print(s1)
print(s2)
print(s3)

print(hex(id(s1)))
print(hex(id(s2)))
print(hex(id(s3)))

# ==와 is의 차이점
print(s1 == s3)     # 값이 동일한지 비교
print(s1 is s3)     # 동일한 객체인지 비교



print('===== immutable vs mutable =====')
n1=10
n2=n1

print(n1 is n2)
print(sys.getrefcount(n2))

n1=n1+1     # n1이 가리키는 객체가 변경됨 (immutable)

print(n1 is n2)
print(sys.getrefcount(n2))




print('===== object interning =====')
# 속성이 동일한 immutable 객체를 공유하는 최적화 기법 (문자열, 작은 범위 정수(버전마다 다름))
n1=100
n2=100
n3=98765678
n4=98765678

print(hex(id(n1)))
print(hex(id(n2)))
print(hex(id(n3)))
print(hex(id(n4)))

n1+=1
n2+=1
n3+=1
n4+=1

print(hex(id(n1)))
print(hex(id(n2)))
print(hex(id(n3)))
print(hex(id(n4)))




print('===== 변수의 삭제 =====')
n1=10
n2=n1

print(sys.getrefcount(n1))

del n2

print(sys.getrefcount(n1))

#print(n2)     # NameError: name 'n2' is not defined




print('===== overflow =====')
n1 = 10
n2 = 10_000_000_000
n3 = 100_000_000_000_000_000_000_000_000_000_000_000_000_000
n4 = n3*n3

print(n3)
print(n4)

print(sys.getsizeof(n1))
print(sys.getsizeof(n2))
print(sys.getsizeof(n3))
print(sys.getsizeof(n4))



print('===== ctypes.Structure 활용 =====')
# 메모리 레이아웃을 C언어와 동일한 방식으로 정의
# C언어와 값을 주고받을 때 사용
class Int(ctypes.Structure):
    _fields_ = [('ob_refcnt', ctypes.c_long),
                ('ob_type', ctypes.c_void_p),
                ('ob_size', ctypes.c_ulong),
                ('ob_digit', ctypes.c_long)]

n1 = 10
p1 = Int.from_address(id(n1))

print(p1.ob_refcnt)   # 참조계수
print(p1.ob_type)     # 타입 객체의 주소
print(p1.ob_size)     # 정수의 자릿수
print(p1.ob_digit)    # 정수의 실제 값 (10진수로 표현된 자릿수)