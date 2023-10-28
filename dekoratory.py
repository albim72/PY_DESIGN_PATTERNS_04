import time

#przykład 1

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        print(f'czas startu: {starttime} s')
        funkcja()
        endtime = time.time()
        print(f'czas końca: {endtime} s')
        print(f"czas wykonania funkcji {funkcja.__name__} wynosi: {endtime-starttime} s")
    return wrapper

def sleepdec(funkcja):
    def wrapper(*args):
        time.sleep(3)
        return funkcja(*args)
    return wrapper


@pomiarczasu
@sleepdec
def biglista():
    sum([i**5 for i in range(10_000_000)])


biglista()

#przykład 2
def debuginfo(funkcja):
    def wrapper(*args,**kwargs):
        print(f"wołana funkcja to {funkcja.__name__}")
        funkcja(*args)
    return wrapper

@debuginfo
def info(i):
    print(f'ważna informacja: {i}')

info(f"kod 545435345")
