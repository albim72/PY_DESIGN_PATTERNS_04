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


@pomiarczasu
def biglista():
    sum([i**5 for i in range(10_000_000)])

biglista()
