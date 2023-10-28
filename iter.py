from dataclasses import dataclass
from collections.abc import Iterable
from typing import List

@dataclass
class Simple:
    field1:str
    field2:int
    field3:float = 1.1

sp = Simple('abc',3445)
# for x in sp:
#     print(x)

print(isinstance(sp,Iterable))
print(isinstance([4,5,7,2],Iterable))
print("_"*40)

@dataclass
class Employee:
    firstname:str
    lastname:str
    accepted:bool = False

@dataclass
class Company:
    name:str

    def __post_init__(self):
        self._employees:List[Employee] = []

    def hire_employee(self,employee:Employee):
        self._employees.append(employee)

    def fire_employee(self,employee:Employee):
        self._employees.remove(employee)

    def __iter__(self):
        return iter(filter(lambda x:x.accepted, self._employees))

first_emp = Employee('Jan','Kot',True)
second_emp = Employee('Janusz','Kotecki')
third_emp = Employee('Olga','Nowak',True)
four_emp = Employee('Nadia','Nowik',True)
four_emp = Employee('Nadia',6456434,True)

company = Company('ABC')
company.hire_employee(first_emp)
company.hire_employee(second_emp)
company.hire_employee(third_emp)
company.hire_employee(four_emp)

for emp in company:
    print(emp)

company.fire_employee(first_emp)
print("usunięcie rekordu!")
for emp in company:
    print(emp)
