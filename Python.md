# 내장 함수 사용

기본적으로 파이썬에 내장되어있는 함수

CPython을 사용하는 경우 Built In Function 사용 시 내부적으로 C언어로 구성되어 있어, 직접 코드작성하는 것 보다 성능이 좋다

<img width="375" height="312" alt="image" src="https://github.com/user-attachments/assets/c6cffae1-247b-47c3-81cc-9f70505a4e4a" />

참고 : https://docs.python.org/ko/3/library/functions.html

# 외부 패키지 설치

외부 모듈을 사용하기 위해 python에 import 해야됨

cmd에 pip install [패키지이름] 입력

# 변수의 특징

- 변수는 선언 없이 사용
- 파이썬에서 변수는 메모리에 놓인 객체를 가리키는 참조(포인터)
- 대입 연산을 수행하면 2개의 변수가 동일 객체를 가리키게 된
- 임의의 변수는 모튼 타입의 객체를 가리킬 수 있다
- 파이썬 정수는 overflow가 없다
