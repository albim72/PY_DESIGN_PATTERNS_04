from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie(self, odl, jedn):
        return jedn*100/odl

    def kosztyprzejazdu(self, odl, jedn, cena_j):
        return self.spalanie(odl,jedn)*(odl/100)*cena_j
