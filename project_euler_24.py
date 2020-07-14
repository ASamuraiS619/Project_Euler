# -*- coding: utf-8 -*-

'''
Problem24 「辞書式順列」

順列とはモノの順番付きの並びのことである. たとえば, 3124は数 1, 2, 3, 4 の一つの順列である. すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ. 0と1と2の順列を辞書順に並べると

        012 021 102 120 201 210
になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?
'''

import time
from functools import reduce

if __name__ == '__main__':
    start = time.time()

    # 1〜9までの数字とその階乗の辞書を作成
    factorials = {}
    for i in range(1, 10):
        factorials[i] = reduce(lambda x, y: x * y, range(1, i+1))

    digits = list(range(10))
    answer = ""
    # 「0番目」から数え始めるので1を引く
    num = 10 ** 6 - 1

    for k in range(9, 0, -1):
        answer += str(digits.pop(num // factorials[k]))
        num = num % factorials[k]
    answer += str(digits[0])

    print(answer)   # answer 2783915460

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 8)) + "[sec]")   # 0.0000618sec
