#przykład 1
def liczby():
    for i in range(17):
        yield i*2

print(liczby())

for p in liczby():
    print(p)

#przykład 2
def wznowienia(n,k):
    print("wstrzymanie działania...")
    yield 1005
    print("wznowienie działania...")

    n=4*n
    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n-k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n/k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n**k
    print("wznowienie działania...")

for i in wznowienia(12,8):
    print("*"*40)
    print(type(i))
    print(f"zwrócono wartość: {i}")
