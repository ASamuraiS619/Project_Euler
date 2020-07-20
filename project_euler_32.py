# -*- coding: utf-8 -*-

'''
Problem32 「Pandigital products」

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
(かける数、かけられる数、積を合わせて9桁のパンデジタルになる積の合計を求めよ。)
'''

import time

# 考えられるパターンは 1桁 × 4桁 = 4桁、2桁 × 3桁 = 4桁 のみ

def is_pandigital(multiplicand, multiplier):
    if multiplier > multiplier:
        multiplicand, multiplier = multiplier, multiplicand
    a = len(str(multiplicand))
    b = len(str(multiplier))
    if (a != 1 or b != 4) and (a != 2 or b != 3):
        return False
    else:
        product = multiplicand * multiplier
        # 積が5桁以上になった場合はFalse
        if product >= 10000:
            return False
        digit_numbers = set(str(product) + str(multiplicand) + str(multiplier))
        # 集合は重複が無いので、0が入っていなくて9つの数字が入っていればOK
        if '0' not in digit_numbers and len(digit_numbers) == 9:
            return True
        else:
            return False

def search_for_pandigital(multiplicand_digit, _sum = 0, pandigital_numbers = []):
    if multiplicand_digit not in {1, 2}:
        return None
    else:
        multiplier_digit = 5 - multiplicand_digit
    for multiplicand in range(10 ** (multiplicand_digit - 1), 10 ** multiplicand_digit):
        for multiplier in range(10 ** (multiplier_digit - 1), 10 ** multiplier_digit):
            if is_pandigital(multiplicand, multiplier):
                product = multiplicand * multiplier
                if product not in pandigital_numbers:
                    _sum += product
                    pandigital_numbers.append(product)
    return _sum, pandigital_numbers


if __name__ == '__main__':
    start = time.time()

    _sum = 0
    # 重複したパンデジタル数は1度だけ足すとのことなので、判定用にリストを用意
    pandigital_numbers = []

    for multiplicand_digit in [1, 2]:
        _sum, pandigital_numbers = search_for_pandigital(multiplicand_digit, _sum, pandigital_numbers)

    print(_sum) # answer 45228
    #  28 ×  157 = 4396
    #  18 ×  297 = 5346
    #  12 ×  483 = 5796
    #   4 × 1738 = 6952
    #  39 ×  186 = 7254
    #  48 ×  159 = 7632
    #   4 * 1738 = 7852

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.14422sec
