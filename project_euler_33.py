# -*- coding: utf-8 -*-

'''
Problem33 「Digit cancelling fractions」

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
(1以下の分数で、分母と分子がともに2桁のものについて、分子と分母それぞれから同じ数字を消した分数が、元の分数と等しくなる分数が4つある。それらの積を約分したものの分母を求めよ。)
'''

import time

numerators = list(range(10, 100))
denominators = list(range(10, 100))

def is_the_curious_fraction(numerator, denominator):
    # 共通するものがない場合はFalse
    # 共通するものが0の場合は 10 / 30 のような分数なので同じくFalse
    numerator_digit_numbers = set(str(numerator))
    denominator_digit_numbers = set(str(denominator))
    common_number = numerator_digit_numbers & denominator_digit_numbers
    if not common_number or common_number == {'0'}:
        return False
    else:
        # ゾロ目の数字(11, 66など)はcommon_numberと一致してしまうので、その場合はcommon_numberを取ってくる
        new_numerator = numerator_digit_numbers ^ common_number or common_number
        new_denominator = denominator_digit_numbers ^ common_number or common_number
        # 新しい分母が0の場合は分数にならないのでFalse
        if int(list(new_denominator)[0]) == 0:
            return False
        elif int(list(new_numerator)[0]) / int(list(new_denominator)[0]) == numerator / denominator:
            return True
        else:
            return False

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    start = time.time()

    product_of_numerators = 1
    product_of_denominators = 1
    for numerator in numerators:
        for denominator in denominators[numerators.index(numerator) + 1:]:
            if is_the_curious_fraction(numerator, denominator):
                product_of_numerators *= numerator
                product_of_denominators *= denominator

    # 最大公約数で割って、答えを出す。
    print(int(product_of_denominators / gcd(product_of_denominators, product_of_numerators)))   # answer 100

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00675sec
