from pojazd import Pojazd

p1 = Pojazd()
odl = 653
jd = 59
cj = 6.34

print(f'spalanie [l/100km]: {p1.spalanie(odl,jd):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {p1.kosztyprzejazdu(odl,jd,cj)} zł')
