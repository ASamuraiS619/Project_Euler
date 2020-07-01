# -*- coding: utf-8 -*-

'''
Problem3 「最大の素因数」

13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
'''

import time

#エラトステネスの篩でnumber以下の素数を列挙
def primes_up_to(number):
    border_line = int(number ** 0.5)
    prime_numbers = [2]
    target_list = list(range(3, number + 1, 2))

    while True:
        candidate = min(target_list)
        if candidate > border_line:
            prime_numbers.extend(target_list)
            break
        prime_numbers.append(candidate)

        tmp = []
        for i in target_list:
            if i % candidate != 0:
                tmp.append(i)
        target_list = tmp

    return prime_numbers

if __name__ == '__main__':
    start = time.time()

    #素因数は最大でも√600851475143以下なので、そこまでの素数で逆順に割っていき、最初に割り切れたのが答え。
    border_line_for_check = int(600851475143 ** 0.5)
    target_primes = sorted(primes_up_to(border_line_for_check), reverse = True)

    for i in target_primes:
        if 600851475143 % i == 0:
            # answer 6857
            print(i)
            break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 3)) + "[sec]")   # 1.31sec
