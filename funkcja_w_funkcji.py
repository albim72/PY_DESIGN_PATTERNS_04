#przykład 1
n=100
def oblicz(a,b,c):
    global n
    n = (a+b)*c + n
    return n

print(oblicz(3,5,3))
print(n)

