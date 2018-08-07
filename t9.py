import functools

def log(func_or_text):
    if isinstance(func_or_text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('begin call ' + func_or_text)
                res = func(*args,**kw)
                print('end call')
                return res
            return wrapper
        return decorator
    else:
        # log无参数，则传进来func_or_text的是函数
        @functools.wraps(func_or_text)
        def wrapper(*args,**kw):
            print('begin call')
            res = func_or_text(*args,**kw)
            print('end call')
            return res
        return wrapper

@log
def f1(x):
    print('This is f1')
    return x*2 

@log('execute')
def f2(x):
    print('This is f2')
    return x*3

print(f1(2))

print(f2(3))
