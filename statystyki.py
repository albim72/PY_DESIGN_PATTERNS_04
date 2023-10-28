liczby = [56,700,-45,6,78,12,-1123,456,56,780,67,10,-112]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum - minimum
    srarytm = sum(dane)/len(dane)

    return minimum,maksimum,rozstep,srarytm

wynik = statystyki(liczby)
print(type(wynik))
print(wynik)

mini,maxi,roz,sa = statystyki(liczby)
print(f'wartość maksymalna: {maxi}, minimalna: {mini}, rozstęp: {roz}, srednia arytmetyczna: {sa}')
