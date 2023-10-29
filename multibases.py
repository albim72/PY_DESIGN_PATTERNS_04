class MultiBases(type):
    def __new__(cls,name,bases,atrs):
        if len(bases) > 1:
            raise TypeError("Wielodziedziczenie w tej klasie jest niemożliwe!")
        return super().__new__(cls,name,bases,atrs)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A):
    pass

class F:
    pass

class Test(F,B):
    pass
