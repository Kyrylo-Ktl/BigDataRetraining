from math import isqrt


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    divisor = 6
    while divisor * divisor <= num + 1:
        if num % (divisor - 1) == 0 or num % (divisor + 1) == 0:
            return False
        divisor = divisor + 6

    return isqrt(num) ** 2 != num


def primes_generator():
    num = 1
    while True:
        if is_prime(num):
            yield num
        num += 1


for num in primes_generator():
    print(num)
