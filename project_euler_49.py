# -*- coding: utf-8 -*-

'''
Problem49 「Prime permutations」

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
(等差数列で連続する3項について、①4桁②3項とも素数③それぞれ互いに数字を並べ替えた形になっている、の3つの性質を兼ね備えたものが1487, 4817, 8147の他にもう一組ある。それら3つの数字を結合した12桁の数字を答えよ。)
'''

import time
from functions import is_prime

def is_permutation_of_the_other(num1, num2):
    if sorted(str(num1)) == sorted(str(num2)):
        return True
    else:
        return False

if __name__ == '__main__':
    start = time.time()

    # 4桁の素数のリストと集合を作っておく
    FOUR_DIGIT_PRIMES = [num for num in range(1001, 10000) if is_prime(num)]
    FOUR_DIGIT_PRIMES_SET = set(FOUR_DIGIT_PRIMES)

    flag = False
    for prime1_index, prime1 in enumerate(FOUR_DIGIT_PRIMES):
        for prime2 in FOUR_DIGIT_PRIMES[prime1_index + 1:]:
            # 例で示されているもの以外で探すので弾く
            if prime1 == 1487:
                pass
            elif is_permutation_of_the_other(prime1, prime2):
                diff = prime2 - prime1
                num3 = prime2 + diff
                if num3 in FOUR_DIGIT_PRIMES_SET and is_permutation_of_the_other(prime1, num3):
                    print(str(prime1) + str(prime2) + str(num3))    # answer 296962999629
                    flag = True
                    break
        if flag == True:
            break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.2491sec
