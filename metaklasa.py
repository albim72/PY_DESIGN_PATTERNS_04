class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attribs):
        print("*"*45)
        print(f'nazwa klasy: {clsname}')
        print(f'dziedziczone klasy: {superclasses}')
        print(f'słownik atrybutów: {attribs}')
        return type.__new__(cls,clsname,superclasses,attribs)

class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    def info(self):
        return True

class B(Specjalna):
    pass

class C(B,F):
    pass
