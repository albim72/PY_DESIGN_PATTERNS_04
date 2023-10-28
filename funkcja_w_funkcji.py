#przykład 1
n=100
def oblicz(a,b,c):
    global n
    n = (a+b)*c + n
    return n

print(oblicz(3,5,3))
print(n)

#przykład 2

def witaj(imie):
    return f'dziękujemy za założenie konta: {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, egzamin zdany? {zaliczono}'

def fx(a,b):
    return a*100/b

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Olga",67,"tak"))
print(osoba(fx,6,7))

liczby = [3,6,78,29,11,12,-15,0,-34,303,19,18,60,101,0,2,-4,221]

parzysta = list(filter(lambda x:x%2==0,liczby))
print(parzysta)

cube = list(map(lambda x:x**3,liczby))
print(cube)

