# 문자열 안에서 " 사용
s1='To be Or "Not" To Be'
s2="To be Or \"Not\" To Be"

# 여러줄 문자열 리터럴
s3 = 'AAA\nBBB\nCCC'
s4 = '''AAA
BBB
CCC'''

'''
적어놓고 사용하지 않는 문자열은 주석으로 간주한다. (docstring)
그래서 여러줄 주석을 적을 때 이 처럼 표기할 수 있다
'''

s5='Python'
s6=s5+s5    # PythonPython
s7=s5*3     # PythonPythonPython

print('='*20) #====================
s8='hello'
print(s8[1])  #e
#s8[1]='a'    # error : 문자열은 immutable이므로 인덱싱으로 요소를 변경할 수 없음

print('o' in s8)   #True
print('llo' in s8)  #True
print(len(s8))      #5

s8.count('l')      #2
s8.find('l')       #2 (첫 번째 'l'의 인덱스)
s8.index('l')      #2 (첫 번째 'l'의 인덱스, 찾지 못하면 ValueError)

s8.find('x')       #-1 (찾지 못하면 -1)
s8.index('x')      #ValueError: substring not found

s9=' hello world '
print('|' + s9 + '|')
print('|' + s9.strip() + '|')   #양쪽 공백 제거
print('|' + s9.lstrip() + '|')  #왼쪽 공백 제거
print('|' + s9.rstrip() + '|')  #오른쪽 공백 제거
print('python is simple'.replace('simple','powerful'))  #문자열 대체
print('/'.join('ABCDEF'))  #문자열 사이에 '/' 삽입하여 연결 -> A/B/C/D/E/F

print('python is simple'.split())  #공백을 기준으로 문자열 분리 -> ['python', 'is', 'simple']
#print('Hello'.len())  #AttributeError: 'str' object has no attribute 'len'
print(len('Hello'))  #5

print('ABCDEFG'[0])  #A
print('ABCDEFG'[4])  #E

print('ABCDEFG'[-1]) #G

# Slice [begin:end:step]
print('ABCDEFG'[slice(1,4)])  #BCD (인덱스 1부터 3까지)
print('ABCDEFG'[slice(None,3)]) #ABC (처음부터 인덱스 2까지)
print('ABCDEFG'[slice(3,None)]) #DEFG (인덱스 3부터 끝까지)
print('ABCDEFG'[slice(None,None,2)]) #ACEG (인덱스 0부터 끝까지 2씩 건너뛰며)
print('ABCDEFG'[slice(None,None,-1)]) #GFEDCBA (문자열을 역으로 출력)

print('ABCDEFG'[1:4])   #BCD (인덱스 1부터 3까지)
print('ABCDEFG'[:3])    #ABC (처음부터 인덱스 2까지)
print('ABCDEFG'[3:])    #DEFG (인덱스 3부터 끝까지)
print('ABCDEFG'[::2])   #ACEG (인덱스 0부터 끝까지 2씩 건너뛰며)
print('ABCDEFG'[::-1])  #GFEDCBA (문자열을 역으로 출력)