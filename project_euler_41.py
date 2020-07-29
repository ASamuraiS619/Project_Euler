# -*- coding: utf-8 -*-

'''
Problem41 「Pandigital prime」

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
(最大のパンデジタルな素数は？)
'''

import time
from functions import is_prime
from itertools import permutations

if __name__ == '__main__':
    start = time.time()

    flag = False
    for length in range(9, 1, -1):
        # (length)桁のパンデジタル数のリストを作成
        # permutationsを使って、まずは順列(タプル)のリストを作成
        pandigital_numbers = list(list(permutations([str(num) for num in range(1, length + 1)])))
        # タプルを結合して数値化
        pandigital_numbers = list(map(lambda x: int(''.join(x)), pandigital_numbers))
        # 大きい順に調べられるよう降順にソート
        pandigital_numbers.sort(reverse=True)
        for pandigital_number in pandigital_numbers:
            if not pandigital_number % 2:
                pass
            elif is_prime(pandigital_number):
                print(pandigital_number)    # answer 7652413
                flag = True
                break

        if flag:
            break



    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.40187sec
