# -*- coding: utf-8 -*-

'''
Problem3 「最大の素因数」

13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
'''

from sympy import sieve

border_line_for_check = int(600851475143 ** 0.5)
target_primes = sorted(sieve.primerange(1, border_line_for_check), reverse = True)

for i in target_primes:
    if 600851475143 % i == 0:
        # answer 6857
        print(i)
        break
