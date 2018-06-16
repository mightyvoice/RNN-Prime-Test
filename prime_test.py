
from math import sqrt


def basic_prime_test(num):
    for x in range(2, int(sqrt(num))+1):
        if num % x == 0:
            return False
    return True


def miller_robin_test(num):
    pass
