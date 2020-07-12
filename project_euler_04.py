# -*- coding: utf-8 -*-

'''
Problem4 「最大の回文積」

左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
'''

import time

def is_palindromic_number(number):
    str_number = str(number)

    # intすると切り捨てになるので、奇数桁にも対応できている。
    for i in range(int(len(str_number) / 2)):
        if str_number[i] != str_number[-(1+i)]:
            return False
    return True


if __name__ == '__main__':
    start = time.time()

    three_digit_numbers = list(range(100, 1000))
    checking_numbers = []

    # checking_numbersに3桁の数の積を全て入れていく
    for i in range(len(three_digit_numbers)):
        for k in range(len(three_digit_numbers) - i):
            # 重複が出ないよう、自分以上の数字とだけ積を取っていく。
            checking_numbers.append(three_digit_numbers[i] * three_digit_numbers[i + k])

    # 大きい順に調べられるよう降順にソート
    checking_numbers.sort(reverse=True)

    for k in checking_numbers:
        if is_palindromic_number(k):
            # answer 906609
            print(k)
            break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.12422sec
