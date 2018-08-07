import functools
def xx(text = None):
     def decorator(func):
          @functools.wraps(func)
          def wrapper(*args,**kw):
               if text == None:
                    print('begin:%s' % (func.__name__))
               else:
                    print('begin: %s %s()' % (text,func.__name__))
               re = func(*args,**kw)
               print('end.',func.__name__)
               return re
          return wrapper
     return decorator

@xx('aaa')
def f():
     print('2016-f')
     return 'f'
   

@xx()
def n():
     print('2016-n')
     return 'n'
    

def x():
    return 'x'

#f()
#print('======================')
#n()

print(f())
print('======================')
print(n())
print(x())

