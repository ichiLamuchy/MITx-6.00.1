

'''
The comments are for studing purpose

Exercise: genPrimes
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

dont need to use name varible "nex" to yield. You can use any variable.

use these code to check.

a = genPrimes()
print(genPrimes())

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
'''



def genPrimes():
    # primes generated so far, this is the only numbers you need to %, because it is the prime number!
    primes = []   
    primeNum = 1      
    while True:
        primeNum += 1
        for p in primes:
            if primeNum % p == 0:
                break
        else:
            primes.append(primeNum)
            yield primeNum
