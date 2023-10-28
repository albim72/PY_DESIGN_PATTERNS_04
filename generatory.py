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

#przykład 3
def genret():
    for i in range(72):
        if i==34:
            print("przerwamy")
            return
        else:
            yield i

for t in genret():
    print(t)

#przykład 4
def complexgen():
    x=0
    while True:
        print("x-print")
        y = yield x
        z = yield 2*x
        print("x-print2")
        if y is None:
            x = x+1
            #z = x+20
        else:
            x=y
            #z = 2*y

g = complexgen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(121))
print(next(g))
print(next(g))
print(next(g))


# for j in complexgen():
#     print(j)
