import time
import builtins

n1 =10
n2=int(10)
n3=int()
n4=int('10')
#n5=int('aa')   #예외 발생 : ValueError

print(dir(int))  #int 클래스의 속성 및 메소드 확인
print(int.mro())  #int 클래스의 상속계층을 list 형태로 출력

print(hex(id(n1)))  #객체의 주소 출력
print(hex(id(int)))  #타입 객체의 주소 출력

DWORD = int
n5=int

n6=DWORD(10)    #DWORD는 int의 별칭이므로 n6는 int 클래스의 인스턴스가 됨
n7=n5(10)       #n5는 int 클래스의 별칭이므로 n7도 int 클래스의 인스턴스가 됨

int=n2
#n8=int(50)  # error : int는 타입이 아님
#print(int)  # n2의 값인 10이 출력됨

def foo(x):
    return float

ret =foo(int)   #함수의 인자로 type을 보낼 수 있고 반환값으로 type을 받을 수 있음
LONG = type(n1) # LONG은 n1의 타입인 int 클래스의 별칭이 됨

print(isinstance(n1,int))   #n1이 int 클래스의 인스턴스인지 확인 (True)
print(isinstance(n1,object)) #n1이 object 클래스의 인스턴스인지 확인 (True)
print(type(n1) is int)  #n1의 타입이 int 클래스인지 확인 (True)
print(type(n1) is object) #n1의 타입이 object 클래스인지 확인 (False)

print(dir(time)) # time 모듈의 모든 속성 및 메소드 확인

f=getattr(time,'time')  # time 모듈에서 'time'이라는 이름의 속성(함수)을 가져옴
f()  # time.time() 함수를 호출하여 현재 시간을 반환

print(dir(builtins)) # builtins 모듈의 모든 속성 및 함수 확인

i=getattr(builtins,'int')  # builtins 모듈에서 'int'라는 이름의 속성(클래스)을 가져옴
n=i(10)  # int(10)과 동일하게 n에 10이 할당됨