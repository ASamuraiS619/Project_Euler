# -*- coding: utf-8 -*-

'''
Problem16 「各位の数字の和」

215 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.
同様にして, 2^1000 の各位の数字の和を求めよ.
'''

from functools import reduce

if __name__ == '__main__':
    target = 2 ** 1000
    answer = reduce(lambda x, y: int(x) + int(y), str(target))
    print(answer)   # answer 1366
