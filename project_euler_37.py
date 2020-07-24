# -*- coding: utf-8 -*-

'''
Problem37 「Truncatable primes」

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

note: 2, 3, 5, and 7 are not considered to be truncatable primes.
(右からでも左からでも、桁を減らしていった数字が全て素数になる全ての素数(11個)の合計は？)
'''

import time
from functions import is_prime

# 左側から「右へ」桁を削っていって最後まで素数か
def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False

    str_prime = str(num)
    length = len(str_prime)

    for i in range(length):
        if not is_prime(int(str_prime[i:])):
            return False
    return True


def is_truncatable_prime(num):
    str_num = str(num)
    length = len(str_num)

    if not is_prime(num):
        return False
    for i in range(length):
        if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:length - i]))):
            return False
    return True

# ①一番上の位は2, 3, 5, 7のいずれか、一の位は3, 7のいずれかでなければならない。
# ②3桁以上の場合は、一番上の桁以外は奇数でなければならない。
# ③一番上の桁を削った数はright_truncatable_primeでなければならない。

if __name__ == '__main__':
    start = time.time()

    # 最初は仮置
    right_truncatable_primes = ['3', '7']
    truncatable_primes = []

    flag = True
    while flag:
        for leading_digit in ['2', '3', '5', '7']:
            for prime in right_truncatable_primes:
                target = int(leading_digit + prime)
                if is_truncatable_prime(target):
                    truncatable_primes.append(target)
                    if len(truncatable_primes) == 11:
                        flag = False

        next_right_truncatable_primes = []
        for odd_num in ['1', '3', '5', '7', '9']:
            if not flag:
                break
            for prime in right_truncatable_primes:
                target = int(odd_num + prime)
                if is_right_truncatable_prime(target):
                    next_right_truncatable_primes.append(str(target))
        right_truncatable_primes = next_right_truncatable_primes

    print(sum(truncatable_primes))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00221sec
