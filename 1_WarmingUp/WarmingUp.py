import functools

# 한줄 주석

'''
여러줄 주석1
'''

"""
여러줄 주석 2
"""

#변수
n1 = 10
n2 = 0x10
s1 = 'Hello'
s2 = "World"

print(s1, s2)

s2 = 3.14

print(s1, s2)

#시퀀스
st = [1,2,3,4]  #list
tp = (1,2,3,4)  #tuple
se = {1,2,3}    #set
dic = {'mon':'월요일','tue':'화요일','wed':'수요일'} #dictionary

print(st[0],tp[1],dic['mon'])

# 제어문
if n1 % 2 == 0:
    print('even')

#반복문
for i in range(10):
    print(i)

cnt=0
while True:
    print('hi')
    cnt = cnt + 1
    if cnt == 3:
        break

#함수
def Add(x,y):
    return x+y

#클래스
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

p=Point(1,2) #객체 생성

#예외처리
try:
    Add(1,2)
except ValueError as e:
    print('Error')

#Generator, Coroutine
def NextOdd():
    n=1
    while True:
        yield n
        n=n+1

#비동기
import asyncio

async def Foo():
    print('Foo 중단... 5초간 대기')
    await asyncio.sleep(5)
    print('foo 재개')

asyncio.run(Foo())