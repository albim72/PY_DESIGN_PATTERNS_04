from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper


def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

class debugMeta(type):
    def __new__(cls, clsname,bases,attrs):
        obj = super().__new__(cls,clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=debugMeta):
    pass

class Calc(Base):
    def add(self,x,y):
        return 2*x+y

    def multi(self,x,y):
        return 10*x*y



mc = Calc()

print(mc.add(4,5))
print(mc.multi(4,5))


print(mc.multi.__name__)
