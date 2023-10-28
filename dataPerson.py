from dataclasses import dataclass,astuple,asdict,field
import datetime

@dataclass
class Person:
    city:str
    year:int = field(init=False)
    firstname:str = "Janek"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(default=age, init=False,repr=False)


    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job}"

    def __str__(self):
        return f"informacja o osobie: {self.full_name}, rok urodzenia: {self.year}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.year = datetime.datetime.now().year  - self.age




os1 = Person("Kraków")
os1.firstname = "Jerzy"
print(os1.firstname)
print(os1)

os2 = Person("Kielce","Roma","Kos",26,"sekretarka")
print(os2)

print(type(os2.full_name))
print(astuple(os2))
print(asdict(os2))


class Film:
    def __init__(self,tytul,rok):
        self.tytul = tytul
        self.rok = rok
        self.danef = tytul + " " + str(rok)


f = Film("Star Wars",1979)
print(f.danef)



