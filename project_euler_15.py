# -*- coding: utf-8 -*-

'''
Problem15 「格子経路」

2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.
では, 20×20 のマス目ではいくつのルートがあるか.
'''

from functools import reduce

if __name__ == '__main__':
    # 答えは40C20
    N = 40
    R = 20
    denominator = reduce(lambda x, y: x * y, list(range(N, R, -1)))
    numerator = reduce(lambda x, y: x * y, range(1, R + 1))
    print(int(denominator / numerator)) # answer 137846528820
