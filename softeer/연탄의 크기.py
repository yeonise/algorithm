import sys
from collections import Counter

n = int(sys.stdin.readline())
radius = [*map(int, sys.stdin.readline().split())]


def prime_factorization(number):
    i = 2
    primes = set()

    while number != 0:

        if number == 1:
            break

        if number % i == 0:
            number = number // i
            primes.add(i)

        else:
            i += 1

    return primes


radius = [*map(prime_factorization, radius)]
results = []

for r in radius:
    results.extend([*r])

print(Counter(results).most_common(1)[0][1])
