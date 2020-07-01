# -*- coding: utf-8 -*-

'''
Problem10 「素数の和」

10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
200万以下の全ての素数の和を求めよ.
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
    print(sum(primes_up_to(2000000)))   # answer 142913828922
    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 3)) + "[sec]")   # 5.842sec
