# -*- coding: utf-8 -*-

'''
Problem30 「Digit fifth powers」

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
(各桁の5乗の和がその数字そのものと等しい数字を全て合計すると？)
'''

import time

def is_equal_to_sum_of_digit_fifth_powers(num):
    sum_of_digit_fifth_powers = sum(map(lambda x: fifth_powers[x], str(num)))
    if sum_of_digit_fifth_powers == num:
        return True
    else:
        return False

if __name__ == '__main__':
    start = time.time()

    # 5乗を毎回計算しなくて良いように用意しておく。
    fifth_powers = {}
    for i in range(10):
        fifth_powers[str(i)] = i ** 5

    # 99999だと5乗の合計は354294, 9999999だと5乗の合計は413343なので同じになりうるのは6桁まで。
    # もっと言うと(9 ** 5) * 4 + (1 ** 2) * 2 = 236198まで。
    answers = []
    for i in range(2, 9 ** 5 * 4 + 1 ** 5 * 2 + 1):
        if is_equal_to_sum_of_digit_fifth_powers(i):
            answers.append(i)

    print(sum(answers))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.27175sec
