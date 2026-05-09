d1 = dict(name='Kim', age=30, city='Seoul') # 딕셔너리 생성
d2 = {'name': 'Kim', 'age': 30, 'city': 'Seoul'} # d1과 동일

d3={'name':'Kim', 'age':30, 'city':'Seoul', 'name':'Lee'} # 중복된 키가 있을 경우 마지막 키의 값이 저장됨

print(d3['name']) #[]연산자를 이요한 요소 접근

# print(d3['weight']) # keyError : 존재하지 않는 키에 접근하려고 할 때 발생하는 에러
print(d3.get('weight')) # None : get 메소드를 이용한 요소 접근, 존재하지 않는 키에 접근할 때 None 반환
print(d3.get('weight', 'Not Found')) # Not Found : get 메소드의 두 번째 인자를 이용하여 존재하지 않는 키에 접근할 때 반환할 값을 지정

d3['height']=100 # 요소 추가
print(d3) # {'name': 'Lee', 'age': 30, 'city': 'Seoul', 'height': 100}

keys=d3.keys() # 딕셔너리의 키를 반환하는 메소드 / <class 'dict_keys'> 객체로 반환
values=d3.values() # 딕셔너리의 값을 반환하는 메소드 / <class 'dict_values'> 객체로 반환
items=d3.items() # 딕셔너리의 키-값 쌍을 반환하는 메소드 / <class 'dict_items'> 객체로 반환

print('age' in d3) # True : 키가 딕셔너리에 존재하는지 확인
d3.clear() # 딕셔너리의 모든 요소 제거