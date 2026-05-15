def Func1(a=10,b=20,*,c=30,d=40):
    '''
    함수에 대한 설명
    '''
    print('Func1')

print(Func1.__doc__)        # 함수에 대한 설명
print(Func1.__name__)       # 함수의 이름
print(Func1.__qualname__)   # 클래스명.함수이름
print(Func1.__defaults__)   # 디폴트 인자 값 (10,20)
print(Func1.__kwdefaults__) # keyward 디폴트 인자 값 {'c':30,'d':40}

def Func2(x,y):
    return x+y

# annotations
# int만 쓸 수 있다는 뜻이 아님
# 추후 고급 기법에서 활용된다고 함
def Func3(x : int, y : int) -> int:
    return x+y

print(Func2.__annotations__)    # {}
help(Func2)                     # Func2(x,y)

print(Func3.__annotations__)    # {'x':<class 'int'>,'y':<class 'int'>,'return':<class 'int'>}
help(Func3)                     # Func3(x:int,y:int)->int

# closure
# py에선 inner함수에서 outer함수의 지역변수에 접근 할 수 있는데 그걸 closure에 저장
def outer(x):
    y=0
    print(hex(id(x)),hex(id(y)))

    def inner():
        nonlocal x,y
        x=10
    return inner

f=outer(10)     # f = inner
print(f.__closure__)    # print(hex(id(x)),hex(id(y)))에 출력된값과 동일

# dict
# 함수도 객체이기 때문에 dictionary형태로 값을 보관할 수 있다
def Func4():
    print('Func4')

print(Func4.__dict__)   # {}
Func4.__dict__['x']=10
print(Func4.__dict__)   # {'x':10}
Func4.y=20              # Func4.__dict__['y']=20이랑 동일
print(Func4.__dict__)   # {'x':10,'y':20}

def Func5():
    print('Func5')

Func4.Func5=Func5       #함수에 함수 등록
Func4.Func5()           #등록된 함수 호출

#built-in-function들은 최적화 되어있어서 몇가지 메소드가 제외되어 있다 (ex. __dict__)