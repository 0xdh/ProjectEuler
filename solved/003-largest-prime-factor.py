from itertools import chain
from math import sqrt

primes = []
number = 600851475143

for num in chain([2], range(3, number, 2)):
    is_prime = True
    square_root = sqrt(num)
    for prime in primes:
        if num % prime == 0:
            is_prime = False
            break
        if prime > square_root:
            break
    if is_prime:
        if number % num == 0:
            print(num)
            while number % num == 0:
                number = int(number / num)
            if number == 1:
                break
        primes.append(num)