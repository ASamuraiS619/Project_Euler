# -*- coding: utf-8 -*-

'''
Problem36 「Double-base palindromes」

The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
(十進数でも二進数でも回文数となっている100万以下の数字の合計を求めよ。)
'''

import time

def is_palindromic_number(str_number):
    # intすると切り捨てになるので、奇数桁にも対応できている。
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-(1+i)]:
            return False
    return True

def is_binary_palindromic_number(str_binary_number):
    # 2進数にすると頭に'0b'が付くのでそれを除いて判定
    binary_num = str_binary_number[2:]
    return is_palindromic_number(binary_num)

if __name__ == '__main__':
    start = time.time()

    # 偶数は2進数の1の位が0になり回文数にはなりえないので、奇数のみ判別。
    answer = sum([num for num in range(1, 10 ** 6, 2) if is_palindromic_number(str(num)) and is_binary_palindromic_number(str(bin(num)))])

    print(answer)  # answer 872187

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.3275sec
