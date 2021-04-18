import math as m
from sys import argv

def isPrime(rg: int) -> bool:
    targ = m.ceil(m.sqrt(rg)) + 1
    i = 3
    while i < targ:
        if rg % i == 0:
            return False
        i += 2
    return True

def endless(i):
    while True:
        yield i
        i += 2
    # return i



def main():

    if len(argv) < 2:
        start = 1
        print("2 ", end="")
        for i in endless(start):
            if isPrime(i):
                print(i, end=" ")

    else:
        targ = int(argv[1])
        start = 3
        print("2 ", end="")
        while start < targ:
            if isPrime(start):
                print(start, end=" ")
            start += 2

main()