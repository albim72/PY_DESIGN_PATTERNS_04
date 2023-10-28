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

mlist = [i**2 for i in liczby]
print(mlist)

dl = [[2,3],[4,5]]
print(dl[1][1])

#przykład 3

def rejestracja(oplata):
    def lista_zawodnikow(nrzawodnika):
        return f'jesteś zawodnikiem nr startowy {nrzawodnika}'
    def brak():
        return 'brak opłaty, uzupełnij w ciągu 3 dni!'
    def error():
        return "błąd kodu wpłaty..."

    if oplata==1:
        return lista_zawodnikow
    elif oplata==0:
        return brak
    else:
        return error

print(rejestracja(1)(677))
print(rejestracja(0)())
print(rejestracja(45)())


#przykład 4
def startstop(funkcja):
    def wrapper(*args):
        print(f"uruchomienie nowej funkcji - {funkcja.__name__}")
        funkcja(*args)
        print("zakończenie działania funkcji...")
    return wrapper

def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka...')

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na torcie urodzinowym')

dmuchanie("świeczek")
