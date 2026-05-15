from functools import partial
from functools import wraps

def register(obj, func=None):
    if func is None:
        return partial(register, obj)   #register 함수에 첫번째 인자값을 obj로 고정하고 register를 다시 호출하게 해준다
    setattr(obj,func.__name__,func)
    return func

def add_emoticon(emoticon=':-)'):
    def decorator(func):
        @wraps(func)        # func이 가지고 있는 metadata를 inner한테 전달해주는 데코레이터
        def inner(*args,**kwargs):
            print(emoticon,'',end='')
            return func(*args,**kwargs)

        @register(inner)    # inner.set_emoticon = set_emoticon : inner함수에 함수 등록
        def set_emoticon(emo):
            nonlocal emoticon
            emoticon=emo
        return inner
    return decorator

@add_emoticon('^_^;')   # say_hello = add_emoticon('^_^;')(say_hello)
def say_hello(name):
    print(f'hello, {name} !')

say_hello('james')
say_hello.set_emoticon('^오^')
say_hello('amy')
