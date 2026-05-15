# 리스트 리턴
def func1():
    return [1,2,3,4,5]

ret = func1() # [1,2,3,4,5]
a,b,c,d,e = func1() # 1,2,3,4,5
a,*b,c=func1() # 1,[2,3,4],5

# 튜플 리턴
def func2():
    return 1,2,3,4,5

ret=func2() #(1,2,3,4,5)
a,b,c,d,e = func2() # 1,2,3,4,5
a,*b,c=func2() # 1,[2,3,4],5

# 리턴값이 없으면 None을 리턴
def func3():
    print('a')

ret = func3() # None

# positional vs keyword (argument)
def func4(a,b,c,d,e):
    print(a,b,c,d,e)

# positional
func4(1,2,3,4,5)

# keyword (순서 변경 가능)
func4(a=1,b=2,d=3,e=4,c=5)

#func4(a=1,b=2,d=3,e=4,5) # 키워드 뒤에 포지셔널 불가능

# 매개변수 /, * 표기
# / : 이 앞으로는 포지셔널만 사용가능
# * : 이 뒤로는 keyword만 사용가능
# 둘 사이는 아무거나 가능
def func5(a,/,b,*,c):
    print(a,b,c)

func5(1,2,3)        # error c는 keyword
func5(a=1,b=2,c=3)  # error a는 positional
func5(1,2,c=3)      # ok
func5(1,b=2,c=3)    # ok

# 디폴트 파라미터
#def func6(a,b=0,c): # error
def func6(a,b=0,*,c): #가능
    print(a,b,c)

# 디폴트 파라미터 주의점
# 함수의 디폴트 파라미터는 __default__라는 속성에 저장되기 때문에 mutable한 값을 사용하면 변할 수 있다
# def func6_1(x=10)     #이건 괜찮
def func6_1(s=[]):
    s.append('#')
    return s

# 안전하게 사용하는 방법
def func6_2(s=None):
    if s is None:
        s=[]
    s.append('#')
    return s

s1=[1,2,3]
print(func6_1(s1))  # [1,2,3,#]
print(func6_1())    # ['#']
print(func6_1())    # ['#','#']
print(func6_1())    # ['#','#','#']

print(func6_2(s1))  # [1,2,3,#]
print(func6_2())    # ['#']
print(func6_2())    # ['#']
print(func6_2())    # ['#']

# unpack
def func7(a,b,c):
    print(a,b,c)

s=[1,2,3]
t=(1,2,3)
d={'a':1,'b':2,'c':3}
d2={'a':1,'b':2,'d':3}

func7(s)    # error
func7(*s)   # ok func7(1,2,3)
func7(*t)   # ok func7(1,2,3)
func7(*d)   # ok func7('a','b','c')
func7(**d)  # ok f1(a=1,b=2,c=3) keyword argument형태로 전달
func7(**d2)  # error f1(a=1,b=2,d=3) d는 없는 인자

# pack
# *args는 tuple로 받게됨(Potisional Argument 전용)
def func8(a,*args):
    print(a,args)

func8(1,2,3,4)  # func8(1,(2,3,4))
func8(1,2,3)    # func8(1,(2,3))
func8(1,2)      # func8(1,(2,))
func8(1)        # func8(1,())

#print의 함수 모양 print(*object, sep=' ',end='\n',file=sys.stdout,flush=False)

# **kwargs는 dictionary로 받게됨(Keyword Argument 전용)
def func9(**kwargs):
    print(kwargs)

func9(a=10,b=20)    #print {'a':10,'b':20}
func9(1,a=10,b=20)  # error

#tuple과 dictionary를 활용한 perfect forwarding
import time
from tkinter import Y

def foo(a,b,c):
    print(a,b,c)
    time.sleep(2)

def goo():
    print('goo')
    time.sleep(3)

def chronometry(f,*args,**kwargs):
    start=time.time()
    f(*args,**kwargs)
    end=time.time()
    print(f'elapsed : {end-start}')

chronometry(goo)
chronometry(foo,1,2,3)
chronometry(foo,1,2,c=3)

# 전역변수, 지역변수
def func10():
    global Y    # 선언되지 않았어도 호출 가능
    global z    # 호출되는순간 생성됨
    x=20        # 지역변수
    y=20        # 전역변수
    z=20        # 전역변수 생성
    print(x)
    print(y)

x=0    
y=0 # func10이 호출되기 전에 생성했으니 func10의 global y는 이걸 가르킴
print(x)
print(y)
#print(z)   # error

func10()

print(x)
print(y)
print(z)

# inner function, nonlocal
g_x = 1

def outer(x):
    y=3

    def inner():
        global g_x     # check의 g_x는 지역변수가 호출된다 하지만 global g_x를 해주면 check에서도 전역변수가 호출된다
        nonlocal x     # 전역변수는 아닌데 지역변수도 아닌 키워드 outer함수 안에서 유효해져 check에서 x=10이 불리게 된다
        g_x=10
        x=10
        y=10

    def check():
        print(g_x,x,y)  # 위 두 키워드가 없을때 출력 : 1,2,3
                        # 위 두 키워드가 있을때 출력 : 10,10,3
    return inner,check

f1,f2=outer(2)

f1()    #inner
f2()    #check