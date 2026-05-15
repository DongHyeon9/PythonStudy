class Car:
    cnt = 0     # 스태틱 맴버 변수 Car.__dic__.cnt 또는 Car.cnt로 사용가능, 객체에서 읽는 건 가능 하지만 쓰기 동작 시 obj.__dic__.cnt에 쓰게 됨 ※주의 필요
    def __init__(self,color=None,speed=None):
        self.x=0    # 맴버 함수 처럼 사용 가능 -> __dict__에 보관
        self._y=0
        self.__z=0  # private 맴버처럼 사용 가능 -> 실제론 _Car__z 로 네임 맹글링 됨 관례상 private처럼 사용
        print('ctor')

    def __del__(self):
        print('dtor')

    def Go():
        print('Go')

    def Stop(self):
        print('Stop')

    def __change_gear():    # private 맴버함수 처럼 사용
        print('Change Gear')

    @staticmethod       # 객체에서도 스태틱 메소드를 호출할 수 있게 도와주는 데코레이터
    def Static_Func():
        print('Static')

    @classmethod        # 1번째 인자로 반드시 클래스 객체를 받아야 한다, 스태틱 메소드를 만들건데 내부적으로 클래스 정보가 필요할 때 사용
    def Class_Func(cls):
        print(cls)

c1=Car()
c2=Car()
Car.Go()
# c1.Go()    # error : c1.Go(c1)

del c2

#Car.Stop() # error : 인자 없음
c1.Stop()

print(c1.__class__)     # 객체의 포인터를 담고있음

Car.Static_Func()
c1.Static_Func()
Car.Class_Func()
c1.Class_Func()
