
from prime_test import *
from random import randint
import glb

all_primes = set([])

all_non_primes = set([])


def get_random_num(only_odd=False):
    res = 0
    for i in range(0, glb.NUM_LEN):
        num = randint(0, 9)
        if i == 0:
            while num == 0:
                num = randint(0, 9)
        if i == glb.NUM_LEN-1 and only_odd:
            while num == 5 or num % 2 == 0:
                num = randint(0, 9)
        res = 10 * res + num
    return res


def get_num_by_order():
    starting_num = 10 ** (glb.NUM_LEN-1) + 1
    while True:
        yield starting_num
        starting_num += 2


def get_all_prime():
    with open(glb.prime_file_name, 'w') as f:
        count = 0
        while count < glb.TOTAL_PRIME_NUM:
            num = get_random_num(True)
            while not basic_prime_test(num):
                num = get_random_num(True)
            count += 1
            f.writelines(str(num)+'\n')
            print(count, num)


def get_all_none_prime():
    with open(glb.none_prime_file_name, 'w') as f:
        count = 0
        while count < glb.TOTAL_NON_PRIME_NUM:
            num = get_random_num(True)
            while basic_prime_test(num):
                num = get_random_num(True)
            count += 1
            f.writelines(str(num)+'\n')
            print(count, num)


def get_all_number():
    f_prime = open(glb.prime_file_name, 'w')
    f_non_prime = open(glb.none_prime_file_name, 'w')
    # num_generator = get_num_by_order()
    while not (len(all_primes) >= glb.TOTAL_PRIME_NUM and len(all_non_primes) >= glb.TOTAL_NON_PRIME_NUM):
        num = get_random_num(True)
        # num = next(num_generator)
        if basic_prime_test(num):
            print('prime: ', num, len(all_primes)+1)
            if len(all_primes) < glb.TOTAL_PRIME_NUM and num not in all_primes:
                all_primes.add(num)
                f_prime.writelines(str(num)+'\n')
        elif len(all_non_primes) < glb.TOTAL_NON_PRIME_NUM and num not in all_non_primes:
            print('not prime: ', num, len(all_non_primes)+1)
            all_non_primes.add(num)
            f_non_prime.writelines(str(num)+'\n')

if __name__ == '__main__':
    # get_all_none_prime()
    # get_all_prime()
    get_all_number()
