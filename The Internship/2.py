from math import sqrt
from itertools import count, islice
import sys
def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def floating_prime(number):
        number = str(number).replace('.','')
        numbers = [int(number[0:i]) for i in range(2,5)]
        checked_numbers = [isprime(i) for i in numbers]
        print(checked_numbers[0] or checked_numbers[1] or checked_numbers[2])

if __name__ == "__main__":
    for line in sys.stdin:
        if line.rstrip() == '0.0':
            break
        elif len(line) > 14:
            raise ValueError('NUMBER MUST NOT EXCEES 12 DIGITS')
        else:
            floating_prime(line)